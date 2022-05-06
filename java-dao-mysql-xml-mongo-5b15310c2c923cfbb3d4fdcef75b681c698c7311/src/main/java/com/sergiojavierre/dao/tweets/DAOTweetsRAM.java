package com.sergiojavierre.dao.tweets;

import com.sergiojavierre.entities.Tweet;

import java.util.ArrayList;
import java.util.List;

public class DAOTweetsRAM implements DAOTweets{
    List<Tweet> listaTweets;

    public DAOTweetsRAM(){
        this.listaTweets = new ArrayList<>();
    }

    @Override
    public void tuitear(Tweet tweet) {
        listaTweets.add(tweet);
    }

    @Override
    public List<Tweet> read() {
        return listaTweets;
    }
}
