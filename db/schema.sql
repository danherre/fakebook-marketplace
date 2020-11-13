PRAGMA foreign_keys = ON;

CREATE TABLE users(
  username VARCHAR(20) NOT NULL,
  fullname VARCHAR(40) NOT NULL,
  email VARCHAR(40) NOT NULL,
  filename VARCHAR(64) NOT NULL,
  password VARCHAR(256) NOT NULL,
  rating FLOAT NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
  PRIMARY KEY(username)
);

CREATE TABLE items(
  itemid INTEGER NOT NULL,
  owner VARCHAR(20) NOT NULL,
  name VARCHAR(40) NOT NULL,
  description VARCHAR(256) NOT NULL,
  price FLOAT NOT NULL,
  image VARCHAR(64) NOT NULL,
  posted DATE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  available BOOLEAN NOT NULL,
  PRIMARY KEY(itemid),
  FOREIGN KEY(owner) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE reviews(
  reviewid INTEGER NOT NULL,
  writer VARCHAR(20) NOT NULL,
  writee VARCHAR(20) NOT NULL,
  review VARCHAR(1024) NOT NULL,
  rating INTEGER,
  created DATE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  PRIMARY KEY(reviewid),
  FOREIGN KEY(writer) REFERENCES users(username) ON DELETE CASCADE,
  FOREIGN KEY(writee) REFERENCES users(username) ON DELETE CASCADE
);
