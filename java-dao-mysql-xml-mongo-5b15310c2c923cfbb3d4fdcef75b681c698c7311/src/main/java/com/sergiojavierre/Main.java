package com.sergiojavierre;

import com.mysql.jdbc.Connection;
import com.sergiojavierre.dao.DAOFactory;
import com.sergiojavierre.entities.User;

import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.List;

public class Main {

    public static void main(String[] args) {


        //User user = new User("sergiojavierre","1234", "sergio@twitter.com");

        //DAOFactory.getInstance().getDaoUsers().register(user);

        User testLogin = new User("sergiojavierre","1234","");
        User resultLogin = DAOFactory.getInstance().getDaoUsers().login(testLogin);
        System.out.println(resultLogin);

        List<User> users = DAOFactory.getInstance().getDaoUsers().read();
        System.out.println(users);


    }

}
