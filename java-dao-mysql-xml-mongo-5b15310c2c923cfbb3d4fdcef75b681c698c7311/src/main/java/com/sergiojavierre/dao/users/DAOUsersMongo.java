package com.sergiojavierre.dao.users;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import com.mongodb.client.MongoDatabase;
import com.mongodb.client.model.Filters;
import com.mongodb.client.result.InsertOneResult;

import com.sergiojavierre.dbs.ConnectionMongo;
import com.sergiojavierre.entities.User;
import org.bson.Document;
import org.bson.conversions.Bson;
import org.bson.types.ObjectId;

import java.util.ArrayList;
import java.util.List;

// Guía: https://www.mongodb.com/docs/drivers/java/sync/current/quick-start/
public class DAOUsersMongo implements DAOUsers{

    MongoDatabase database;
    private final String collection = "users";

    public DAOUsersMongo(){
        this.database = ConnectionMongo.getConnection();
    }

    @Override
    public Boolean register(User user) {
        try {
            MongoCollection<Document> collection = database.getCollection(this.collection);
            InsertOneResult result = collection.insertOne(new Document()
                    .append("_id", new ObjectId())
                    .append("alias", user.getAlias())
                    .append("password", user.getPassword())
                    .append("email", user.getEmail()));
            System.out.println("Success! Inserted document id: " + result.getInsertedId());
        } catch (Exception me) {
            System.err.println("Unable to insert due to an error: " + me);
            return false;
        }
        return true;
    }

    @Override
    public User login(User user) {
        try {
            MongoCollection<Document> collection = database.getCollection(this.collection);
            Bson filter = Filters.and(
                    Filters.eq("alias", user.getAlias()),
                    Filters.eq("password", user.getPassword())
            );
            Document result = collection.find(filter).first();
            if (result != null) {
                return new User(result.getString("alias"), result.getString("email"));
            }
            return null;
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }
        return null;
    }

    @Override
    public List<User> read() {
        try {
            List<User> users = new ArrayList<>();
            MongoCollection<Document> collection = database.getCollection(this.collection);
            try (MongoCursor<Document> cursor = collection.find().cursor()) {
                while (cursor.hasNext()) {
                    Document document = cursor.next();
                    User user = new User(document.getString("alias"), document.getString("email"));
                    users.add(user);
                }
            }
            return users;
        }
        catch (Exception e){
            System.out.println(e.getMessage());
        }
        return null;
    }
}
