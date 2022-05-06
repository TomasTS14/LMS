package com.sergiojavierre.entities;

public class User {
    private String alias, password, email;

    public User(String alias, String email){
        this.alias = alias;
        this.email = email;
    }

    public User(String alias, String password, String email) {
        this.alias = alias;
        this.password = password;
        this.email = email;
    }

    public String getAlias() {
        return alias;
    }

    public String getPassword() {
        return password;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public String toString() {
        return "User{" +
                "alias='" + alias + '\'' +
                ", email='" + email + '\'' +
                '}';
    }
}
