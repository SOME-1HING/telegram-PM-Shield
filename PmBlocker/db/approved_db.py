from . import db

approvedDB = db.approvedDB


async def is_user_approved(user_id: int) -> bool:
    user = approvedDB.find_one({"user_id": user_id})
    if not user:
        return False
    return True


async def get_approved_users() -> list:
    users_list = []
    for user in approvedDB.find({"user_id": {"$gt": 0}}):
        users_list.append(user)
    return users_list


async def add_approved_user(user_id: int):
    is_approved = approvedDB(user_id)
    if is_approved:
        return
    return approvedDB.insert_one({"user_id": user_id})


async def remove_approved_user(user_id: int):
    is_approved = approvedDB(user_id)
    if not is_approved:
        return
    return approvedDB.delete_one({"user_id": user_id})
