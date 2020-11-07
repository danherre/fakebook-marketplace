PRAGMA foreign_keys = ON;

CREATE TABLE users(
  username VARCHAR(20) NOT NULL,
  fullname VARCHAR(40) NOT NULL,
  email VARCHAR(40) NOT NULL,
  filename VARCHAR(64) NOT NULL,
  password VARCHAR(256) NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
  PRIMARY KEY(username)
);

CREATE TABLE items(
);

CREATE TABLE transactions(
  transactionid INTEGER NOT NULL,
  price DOUBLE(6, 2) NOT NULL,
  title VARCHAR(64) NOT NULL,
  filename VARCHAR(64) NOT NULL,
  owner VARCHAR(20) NOT NULL,
  accepter VARCHAR(20),
  description VARCHAR(256) NOT NULL,
  created DATE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  PRIMARY KEY(transactionid),
  FOREIGN KEY (accepter) REFERENCES users(username),
  FOREIGN KEY(owner) REFERENCES users(username) ON DELETE CASCADE
);

CREATE TABLE reviews(
  reviewid INTEGER NOT NULL,
  writer VARCHAR(20) NOT NULL,
  writee VARCHAR(20) NOT NULL,
  text VARCHAR(1024) NOT NULL,
  created DATE DEFAULT CURRENT_TIMESTAMP NOT NULL,
  PRIMARY KEY(reviewid),
  FOREIGN KEY(writer) REFERENCES users(username) ON DELETE CASCADE,
  FOREIGN KEY(writee) REFERENCES users(username) ON DELETE CASCADE
);



