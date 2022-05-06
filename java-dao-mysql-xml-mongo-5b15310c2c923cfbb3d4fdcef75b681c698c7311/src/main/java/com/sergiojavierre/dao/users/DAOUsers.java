package com.sergiojavierre.dao.users;

import com.sergiojavierre.entities.User;

import java.util.List;

public interface DAOUsers {

    public Boolean register(User user);
    public User login(User user);
    public List<User> read();

}
