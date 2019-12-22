CREATE DATABASE stock;

use stock

CREATE TABLE categories (
    id INT auto_increment primary key,
    nom  VARCHAR(50) NOT NULL
)
ENGINE=INNODB;


CREATE TABLE  produits (
    id INT auto_increment primary key,
    nom VARCHAR(30) NOT NULL,
    quantite INT NOT NULL,
    date_expiration DATE,
    prix INT,
    id_categorie INT,
    FOREIGN KEY (id_categorie) REFERENCES categories(id)
) ENGINE=INNODB;

