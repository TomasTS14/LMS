package com.sergiojavierre.entities;

import java.util.Date;

public class Tweet {

    private String content;
    private Date timestamp;
    private User user;

    public Tweet(String content, Date timestamp, User user) {
        this.content = content;
        this.timestamp = timestamp;
        this.user = user;
    }

    public String getContent() {
        return content;
    }

    public Date getTimestamp() {
        return timestamp;
    }

    public User getUser() {
        return user;
    }
}
