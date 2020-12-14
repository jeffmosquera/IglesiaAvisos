db.createUser(
    {
        user: "master",
        pwd: "master1234",
        roles: [
            { role: "readWrite", db: "iglesiaDB" }
        ]
    }
);