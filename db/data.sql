INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (1, 'mgropper', 'Apple Computer', '1 year old MacBook Pro', 100, 'apple.jpg', True, 'Tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (2, 'amanzhan', 'Bicycle', 'Old bike', 10, 'bike.jpg', True, 'Sports');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (3, 'etkoren', 'Camera', '5 year old Canon DSLR', 25, 'camera.jpeg', True, 'Tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (4, 'peteryu', 'Guitar', 'This is a vintage Yamaha guitar in prime condition.', 100, 'guitar.jpg', True, 'Music');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (5, 'danherre', 'Microphone', 'Unused blue yeti microphone', 50, 'mic.jpeg', True, 'Tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (6, 'mgropper', 'Motorcyle', '2018 Harley Davidson', 150, 'motorcycle.jpeg', True, 'Cars');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (7, 'amanzhan', 'Paddle Boards', 'Set of 3 paddle boards', 100, 'paddle.jpg', True, 'Sports');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (8, 'etkoren', 'Skateboard', 'Skateboard in decent condition', 20, 'skateboard.jpeg', True, 'Sports');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (9, 'peteryu', 'Toolbox', 'Set of tools containing a hammer, wrenches, pliers, and a screwdriver', 20, 'tools.jpg', True, 'Tools');


INSERT INTO reviews(reviewid, writer, writee, review)
VALUES (1, 'amanzhan', 'mgropper', 'This product was horrible! Never trust this person.');

INSERT INTO reviews(reviewid, writer, writee, review, rating)
VALUES (2, 'etkoren', 'danherre', 'Would be rated higher, if I could waste more money.', 7);

INSERT INTO reviews(reviewid, writer, writee, review)
VALUES (3, 'peteryu', 'etkoren', 'This is a bot account, dont trust.');

INSERT INTO reviews(reviewid, writer, writee, review)
VALUES (4, 'danherre', 'amanzhan', 'Ok.');

INSERT INTO reviews(reviewid, writer, writee, review)
VALUES (5, 'mgropper', 'peteryu', 'This person lied in their review, I am totally legit!');


INSERT INTO users(username, fullname, email, filename, password, rating)
VALUES ('mgropper', 'Matt Gropper', 'mgropper@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 0.0);

INSERT INTO users(username, fullname, email, filename, password, rating)
VALUES ('amanzhan', 'Amanda Zhang', 'amanzhan@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 0.0);

INSERT INTO users(username, fullname, email, filename, password, rating)
VALUES ('etkoren', 'Etan Koren', 'etkoren@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 0.0);

INSERT INTO users(username, fullname, email, filename, password, rating)
VALUES ('peteryu', 'Peter Yu', 'peteryu@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 0.0);

INSERT INTO users(username, fullname, email, filename, password, rating)
VALUES ('danherre', 'Danny Herrerias', 'danherre@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8', 0.0);
