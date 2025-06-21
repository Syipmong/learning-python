# Week 12: Database Integration

## Learning Objectives
By the end of this week, you will be able to:
- Work with SQLite databases using Python's sqlite3 module
- Perform CRUD operations (Create, Read, Update, Delete)
- Use SQLAlchemy ORM for database operations
- Design and implement database schemas
- Handle database transactions and errors

## Daily Breakdown

### Day 1: SQLite Basics
- SQLite introduction and setup
- Creating databases and tables
- Basic SQL operations with sqlite3
- **Practice**: Personal finance database

### Day 2: CRUD Operations
- Insert, Select, Update, Delete operations
- Parameterized queries and SQL injection prevention
- Working with cursors and connections
- **Practice**: Book library database

### Day 3: SQLAlchemy ORM Introduction
- ORM concepts and benefits
- Setting up SQLAlchemy
- Defining models and relationships
- **Practice**: User management system

### Day 4: Advanced SQLAlchemy
- Relationships (One-to-Many, Many-to-Many)
- Querying with SQLAlchemy
- Migrations and schema updates
- **Practice**: Blog system with relationships

### Day 5: Database Design and Optimization
- Database normalization principles
- Indexing and performance optimization
- Connection pooling and transactions
- **Practice**: E-commerce database design

### Weekend Project: Complete Inventory Management System
Build a full-featured inventory system with SQLAlchemy, including products, categories, suppliers, and transaction history.

## Key Concepts

### SQLite with sqlite3
```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def database_connection(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Access columns by name
    try:
        yield conn
    finally:
        conn.close()

def create_users_table():
    with database_connection('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

def insert_user(username, email):
    with database_connection('example.db') as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (username, email) VALUES (?, ?)',
                (username, email)
            )
            conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError as e:
            print(f"Error inserting user: {e}")
            return None

def get_all_users():
    with database_connection('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users ORDER BY created_at DESC')
        return [dict(row) for row in cursor.fetchall()]

def update_user(user_id, username=None, email=None):
    with database_connection('example.db') as conn:
        cursor = conn.cursor()
        updates = []
        params = []
        
        if username:
            updates.append('username = ?')
            params.append(username)
        if email:
            updates.append('email = ?')
            params.append(email)
        
        if updates:
            params.append(user_id)
            query = f'UPDATE users SET {", ".join(updates)} WHERE id = ?'
            cursor.execute(query, params)
            conn.commit()
            return cursor.rowcount > 0
        return False

def delete_user(user_id):
    with database_connection('example.db') as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        return cursor.rowcount > 0
```

### SQLAlchemy Setup
```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Database setup
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True for SQL logging
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database session context manager
@contextmanager
def get_db_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
```

### SQLAlchemy Models
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    posts = relationship("Post", back_populates="author")
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # Relationship
    author = relationship("User", back_populates="posts")
    
    def __repr__(self):
        return f"<Post(title='{self.title}', author='{self.author.username}')>"

# Create tables
Base.metadata.create_all(bind=engine)
```

### CRUD Operations with SQLAlchemy
```python
class UserService:
    @staticmethod
    def create_user(username: str, email: str) -> User:
        with get_db_session() as session:
            user = User(username=username, email=email)
            session.add(user)
            session.flush()  # Get the ID without committing
            session.refresh(user)  # Refresh to get the ID
            return user
    
    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        with get_db_session() as session:
            return session.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        with get_db_session() as session:
            return session.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_all_users(skip: int = 0, limit: int = 100) -> List[User]:
        with get_db_session() as session:
            return session.query(User).offset(skip).limit(limit).all()
    
    @staticmethod
    def update_user(user_id: int, **kwargs) -> Optional[User]:
        with get_db_session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                for key, value in kwargs.items():
                    if hasattr(user, key):
                        setattr(user, key, value)
                session.flush()
                session.refresh(user)
                return user
            return None
    
    @staticmethod
    def delete_user(user_id: int) -> bool:
        with get_db_session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                return True
            return False

class PostService:
    @staticmethod
    def create_post(title: str, content: str, user_id: int) -> Post:
        with get_db_session() as session:
            post = Post(title=title, content=content, user_id=user_id)
            session.add(post)
            session.flush()
            session.refresh(post)
            return post
    
    @staticmethod
    def get_posts_by_user(user_id: int) -> List[Post]:
        with get_db_session() as session:
            return session.query(Post).filter(Post.user_id == user_id).all()
    
    @staticmethod
    def get_post_with_author(post_id: int) -> Optional[Post]:
        with get_db_session() as session:
            return session.query(Post).options(
                joinedload(Post.author)
            ).filter(Post.id == post_id).first()
```

### Advanced Querying
```python
from sqlalchemy.orm import joinedload
from sqlalchemy import and_, or_, func

class AdvancedQueries:
    @staticmethod
    def search_users(search_term: str):
        with get_db_session() as session:
            return session.query(User).filter(
                or_(
                    User.username.contains(search_term),
                    User.email.contains(search_term)
                )
            ).all()
    
    @staticmethod
    def get_users_with_post_count():
        with get_db_session() as session:
            return session.query(
                User,
                func.count(Post.id).label('post_count')
            ).outerjoin(Post).group_by(User.id).all()
    
    @staticmethod
    def get_recent_posts_with_authors(days: int = 7):
        from datetime import datetime, timedelta
        cutoff_date = datetime.utcnow() - timedelta(days=days)
        
        with get_db_session() as session:
            return session.query(Post).options(
                joinedload(Post.author)
            ).filter(
                Post.created_at >= cutoff_date
            ).order_by(Post.created_at.desc()).all()
    
    @staticmethod
    def bulk_update_posts(user_id: int, **updates):
        with get_db_session() as session:
            affected_rows = session.query(Post).filter(
                Post.user_id == user_id
            ).update(updates)
            return affected_rows
```

## Many-to-Many Relationships
```python
# Association table for many-to-many relationship
from sqlalchemy import Table

post_tags = Table(
    'post_tags',
    Base.metadata,
    Column('post_id', Integer, ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    
    # Many-to-many relationship
    posts = relationship("Post", secondary=post_tags, back_populates="tags")

# Update Post model
class Post(Base):
    # ... existing columns ...
    
    # Many-to-many relationship
    tags = relationship("Tag", secondary=post_tags, back_populates="posts")

# Usage
def add_tags_to_post(post_id: int, tag_names: List[str]):
    with get_db_session() as session:
        post = session.query(Post).filter(Post.id == post_id).first()
        if not post:
            return False
        
        for tag_name in tag_names:
            tag = session.query(Tag).filter(Tag.name == tag_name).first()
            if not tag:
                tag = Tag(name=tag_name)
                session.add(tag)
            
            if tag not in post.tags:
                post.tags.append(tag)
        
        return True
```

## Database Migrations
```python
# Using Alembic for migrations
# pip install alembic

# Initialize Alembic
# alembic init alembic

# alembic.ini configuration
# sqlalchemy.url = sqlite:///example.db

# env.py configuration
from your_models import Base
target_metadata = Base.metadata

# Create migration
# alembic revision --autogenerate -m "Add user table"

# Apply migration
# alembic upgrade head

# Migration file example
def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('users')
```

## Database Performance Optimization

### Indexing
```python
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    # Composite index
    __table_args__ = (
        Index('idx_username_email', 'username', 'email'),
    )
```

### Query Optimization
```python
# Eager loading to avoid N+1 queries
posts_with_authors = session.query(Post).options(
    joinedload(Post.author)
).all()

# Lazy loading vs eager loading
user = session.query(User).options(
    selectinload(User.posts)  # Load posts in separate query
).first()

# Batch operations
def bulk_insert_users(users_data):
    with get_db_session() as session:
        session.bulk_insert_mappings(User, users_data)
```

### Connection Pooling
```python
from sqlalchemy.pool import QueuePool

# Configure connection pool
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,  # Validate connections before use
    pool_recycle=3600    # Recycle connections after 1 hour
)
```

## Best Practices

### Database Design
- Use appropriate data types
- Implement proper indexing
- Normalize data structure
- Use foreign key constraints
- Plan for scalability

### SQLAlchemy Best Practices
- Use context managers for sessions
- Implement proper error handling
- Use lazy loading appropriately
- Batch operations for bulk data
- Keep sessions short-lived

### Security
- Always use parameterized queries
- Validate input data
- Implement proper authentication
- Use database user permissions
- Regular backups

## Assessment
- [ ] Can work with SQLite databases effectively
- [ ] Comfortable with CRUD operations
- [ ] Understands SQLAlchemy ORM concepts
- [ ] Can design normalized database schemas
- [ ] Implements proper error handling
- [ ] Understands performance optimization
- [ ] Completed the weekend project

---
**Previous**: [Week 11: Testing and Debugging](../week-11-testing-debugging/) | **Next**: [Week 13: Specialization Phase](../../04-specialization/)
