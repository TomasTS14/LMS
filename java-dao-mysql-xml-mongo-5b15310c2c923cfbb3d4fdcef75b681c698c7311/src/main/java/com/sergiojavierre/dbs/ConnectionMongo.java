package com.sergiojavierre.dbs;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoDatabase;

public class ConnectionMongo {

    private static MongoClient mongoClient;
    private static String uri = "mongodb://localhost:27017";
    private static String database = "twitter";

    private ConnectionMongo(){}

    public static MongoDatabase getConnection() {
        try {
            if (mongoClient == null) {
                mongoClient = MongoClients.create(uri);
            }
            return mongoClient.getDatabase(database);
        }
        catch (Exception e){
            System.out.println(e.getMessage());
            return null;
        }
    }

}
