package com.sergiojavierre.dbs;

import com.mysql.jdbc.Connection;

import java.sql.DriverManager;
import java.sql.SQLException;

public class ConnectionMySQL {

    private static Connection connection = null;
    private static String IP = "192.168.8.26", database = "twitter", user="elon", password="1234";
    private static String uri = "jdbc:mysql://" + IP + "/" + database + "?characterEncoding=utf8&" +
            "user=" + user + "&password=" + password;
    private ConnectionMySQL(){}

    public static Connection getConnection(){
        if(connection == null){
            try {
                connection = (Connection) DriverManager.getConnection(uri);
            } catch (
                    SQLException ex) {
                // handle any errors
                System.out.println("SQLException: " + ex.getMessage());
                System.out.println("SQLState: " + ex.getSQLState());
                System.out.println("VendorError: " + ex.getErrorCode());
            }
        }
        return connection;
    }


}
