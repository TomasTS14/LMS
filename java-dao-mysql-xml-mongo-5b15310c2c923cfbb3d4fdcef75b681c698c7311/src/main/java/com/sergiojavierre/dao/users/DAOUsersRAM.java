package com.sergiojavierre.dao.users;

import com.sergiojavierre.entities.User;

import java.util.ArrayList;
import java.util.List;

public class DAOUsersRAM implements DAOUsers{

    List<User> users;

    public DAOUsersRAM(){
        this.users = new ArrayList<>();
    }

    @Override
    public Boolean register(User user) {
        Boolean found = false;
        for (int i = 0; i < users.size(); i++) {
            User currentUser = users.get(i);
            if(currentUser.getAlias().equals(user.getAlias())){
                return false;
            }
        }
        if(!found){
            this.users.add(user);
            return true;
        }
        return false;
    }

    @Override
    public User login(User user) {
        for (int i = 0; i < users.size(); i++) {
            User currentUser = users.get(i);
            if(
               user.getAlias().equals(currentUser.getAlias())
                       &&
               user.getPassword().equals(currentUser.getPassword())
            ){
                return currentUser;
            }
        }
        return null;
    }

    @Override
    public List<User> read() {
        return this.users;
    }
}
