package com.sergiojavierre.dao;

import com.sergiojavierre.dao.users.DAOUsers;
import com.sergiojavierre.dao.users.DAOUsersMongo;


public class DAOFactory {

    private static DAOFactory daoFactory;
    //entities
    private DAOUsers daoUsers;

    private DAOFactory(){}

    public static DAOFactory getInstance() {
        if(daoFactory==null){
            daoFactory = new DAOFactory();
        }
        return daoFactory;
    }

    public DAOUsers getDaoUsers(){
        if(this.daoUsers == null){
            this.daoUsers = new DAOUsersMongo();
        }
        return this.daoUsers;
    }

}
