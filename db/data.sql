INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (1, 'mgropper', 'Apple Computer', '1 year old MacBook Pro', 100, 'apple.jpg', True, 'tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (2, 'amanzhan', 'Bicycle', 'Old bike', 10, 'bike.jpg', True, 'sports');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (3, 'etkoren', 'Camera', '5 year old Canon DSLR', 25, 'camera.jpeg', True, 'tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (4, 'peteryu', 'Guitar', 'This is a vintage Yamaha guitar in prime condition.', 100, 'guitar.jpg', True, 'music');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (5, 'danherre', 'Microphone', 'Unused blue yeti microphone', 50, 'mic.jpeg', True, 'tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (6, 'mgropper', 'Motorcyle', '2018 Harley Davidson', 150, 'motorcycle.jpeg', True, 'cars');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (7, 'amanzhan', 'Paddle Boards', 'Set of 3 paddle boards', 100, 'paddle.jpg', True, 'sports');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (8, 'etkoren', 'Skateboard', 'Skateboard in decent condition', 20, 'skateboard.jpeg', True, 'sports');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (9, 'peteryu', 'Toolbox', 'Set of tools containing a hammer, wrenches, pliers, and a screwdriver', 20, 'tools.jpg', True, 'tools');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (10, 'peteryu', 'iPhone 8', 'iPhone 8 64GB in great condition', 10, 'iphoneimage.jpg', False, 'tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (11, 'danherre', 'GoPro Camera', 'GoPro camera in great condition', 25, 'gopro.jpg', True, 'tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (12, 'amanzhan', 'Bose Headphones', 'Bose headphones, cannot hear out of 1 side', 12, 'headphones.jpeg', True, 'tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (13, 'mgropper', 'Apple Keyboard', 'Apple keyboard with a wire', 10, 'keyboard.jpeg', False, 'tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (14, 'etkoren', 'iPad 3', 'My iPad is in horrible condition', 2, 'usedipad.jpg', True, 'tech');

INSERT INTO items(itemid, owner, name, description, price, image, available, category)
VALUES (15, 'danherre', 'TI 84 calculator', 'Use my calculator for physics class you will love it', 25, 'calculator.jpeg', True, 'tech');

INSERT INTO reviews(reviewid, writer, writee, review, rating)
VALUES (1, 'peteryu', 'mgropper', 'Eh, it was okay.', 4);

INSERT INTO reviews(reviewid, writer, writee, review, rating)
VALUES (2, 'amanzhan', 'mgropper', 'This product was horrible! Never trust this person.', 2);

INSERT INTO reviews(reviewid, writer, writee, review, rating)
VALUES (3, 'etkoren', 'danherre', 'Would be rated higher, if I could waste more money.', 7);

INSERT INTO reviews(reviewid, writer, writee, review, rating)
VALUES (4, 'peteryu', 'etkoren', 'This is a bot account, dont trust.', 1);

INSERT INTO reviews(reviewid, writer, writee, review, rating)
VALUES (5, 'danherre', 'amanzhan', 'Ok.', 5);

INSERT INTO reviews(reviewid, writer, writee, review, rating)
VALUES (6, 'mgropper', 'peteryu', 'This person lied in their review, I am totally legit!', 1);

INSERT INTO users(username, fullname, email, filename, password)
VALUES ('mgropper', 'Matt Gropper', 'mgropper@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8');

INSERT INTO users(username, fullname, email, filename, password)
VALUES ('amanzhan', 'Amanda Zhang', 'amanzhan@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8');

INSERT INTO users(username, fullname, email, filename, password)
VALUES ('etkoren', 'Etan Koren', 'etkoren@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8');

INSERT INTO users(username, fullname, email, filename, password)
VALUES ('peteryu', 'Peter Yu', 'peteryu@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8');

INSERT INTO users(username, fullname, email, filename, password)
VALUES ('danherre', 'Danny Herrerias', 'danherre@umich.edu', 'tempProfilePic.png','sha512$a45ffdcc71884853a2cba9e6bc55e812$c739cef1aec45c6e345c8463136dc1ae2fe19963106cf748baf87c7102937aa96928aa1db7fe1d8da6bd343428ff3167f4500c8a61095fb771957b4367868fb8');
