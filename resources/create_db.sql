-- mysql docker image yaml file does not support creation multiple database during initializing

-- create databases
CREATE DATABASE IF NOT EXISTS `airbnb_host` DEFAULT CHARACTER SET utf8;
CREATE DATABASE IF NOT EXISTS `airbnb_user` DEFAULT CHARACTER SET utf8;
CREATE DATABASE IF NOT EXISTS `airbnb_location` DEFAULT CHARACTER SET utf8;

-- create loplat-analytics user and grant rights
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
