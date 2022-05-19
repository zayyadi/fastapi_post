from multiprocessing import synchronize
from fastapi import APIRouter, status, Response, HTTPException, Depends
from app import oauth2, database, models
from app.schema import Vote

from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/vote",
    tags=["vote"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(
    vote: Vote,
    db: Session = Depends(database.get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    """
    Vote for a post
    """
    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id: {vote.post_id} not found ",
        )

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id
    )
    fount_vote = vote_query.first()
    if vote.dir == 1:
        if fount_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="You already voted for this post",
            )
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"Message": "Vote created"}
    else:
        if not fount_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Vote does not exist"
            )

        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"Message": "Vote deleted"}
