CREATE TABLE spells (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE,
    description VARCHAR(255),
    mana_cost INT NOT NULL check (0<=mana_cost and mana_cost<=20)
);