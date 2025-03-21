from models.models import UserModel, User, CreateUser, UpdateUser
from services.base import DbConnection  
from typing import List, Dict, Union, Optional

class UserService(DbConnection):
    def __init__(self):
        super().__init__()
    #retrives users from DB
    def get_users(self, user_id: Optional[int] = None) -> Union[List[User], User]:
        session = self.connection
        
        if user_id:
            #fetching single user
            query = session.query(UserModel).filter(UserModel.id == user_id)
            result = query.first()
            if result:
                return User(id=result.id, name=result.name)
            return None
        #multiple users
        else:
            query = session.query(UserModel)
            result = query.all()
            return [User(id=row.id, name=row.name) for row in result]
    #retrive the list of createuser objects
    def create_users(self, users: List[CreateUser])-> List[User]:
        session = self.connection
        #maps the model objects here 
        user_models = []
        for user in users:
            # Use the ID from the input data
            user_model = UserModel(id=user.id, name=user.name)
            user_models.append(user_model)
        #add all the created users 
        session.add_all(user_models)
        session.commit()
            
        return [User(id=user.id, name=user.name) for user in user_models]
    #delete method for single id deletion
    def delete_user_by_id(self, user_id: int) -> Dict[str, str]:
        session = self.connection
        
        #removes data in usermodel
        user = session.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            return {"error": "User ID not found"}

        #delete the data in that session    
        session.delete(user)
        session.commit()
        return {"message": f"User with ID {user_id} deleted successfully"}
       
    def delete_all_users(self) -> Dict[str, str]:
        session = self.connection
        #delete the data from user model
        session.query(UserModel).delete()
        #commiting the changes
        session.commit()
        return {"message": "All Users Deleted Successfully!"}
 
    def update_user(self, user_id: int, user: UpdateUser) -> Union[Dict[str, str], User]:
        try:
            session = self.connection
            #returns the first result
            user_model = session.query(UserModel).filter(UserModel.id == user_id).first()
            
            #check for user
            if not user_model:
                return {"error": "User not found"}

            #converting the updateuser model to dictionary that are explicitely set
            update_data = user.dict(exclude_unset=True)
            #if data exists
            if update_data:
                #{key,value} pairs
                for key, value in update_data.items():

                    #setting the attribute key of model instance to value
                    setattr(user_model, key, value)
                session.commit()
                # Return updated user data
                return User(id=user_model.id, name=user_model.name)
            else:
                #no data
                return {"error": "No update data provided"}
        except Exception as e:
            return {"error": f"Failed to update user: {str(e)}"}

 
    def update_all_users(self, user: UpdateUser) -> Dict[str, str]:
        session = self.connection
        #converts the user model to dictionary
        update_data = user.dict(exclude_unset=True)
        
        #if any data
        if update_data:
            #update bulk users
            session.query(UserModel).update(update_data)
            #revert the changes
            session.commit()
            return {"message": "All users updated successfully"}
        else:
            return {"error": "No update data provided"}
