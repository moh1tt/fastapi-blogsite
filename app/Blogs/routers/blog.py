from fastapi import APIRouter, Depends, status, HTTPException
from typing import List

from Blogs.hashing import Hash
from Blogs import schemas, database, models, oauth2
from sqlalchemy.orm import Session

router = APIRouter(
     prefix = '/blogs',
     tags=['Blogs']
)

@router.get('/', response_model=List[schemas.ShowBlog])
def all_blogs(db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id,db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{id} id not found')
    
    return blog

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return {'Deleted'}

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(database.get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found")
   
    blog.update(request.dict())
    db.commit()
    return 'Updated'

