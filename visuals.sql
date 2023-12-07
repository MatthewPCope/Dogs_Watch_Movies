-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema visuals
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `visuals` ;

-- -----------------------------------------------------
-- Schema visuals
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `visuals` DEFAULT CHARACTER SET utf8 ;
USE `visuals` ;

-- -----------------------------------------------------
-- Table `visuals`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `visuals`.`users` ;

CREATE TABLE IF NOT EXISTS `visuals`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `visuals`.`visuals`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `visuals`.`visuals` ;

CREATE TABLE IF NOT EXISTS `visuals`.`visuals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `genre` VARCHAR(45) NOT NULL,
  `approved` TINYINT NULL,
  `NoWhy` VARCHAR(255) NULL,
  `notes` VARCHAR(255) NULL,
  `rating` VARCHAR(45) NULL,
  `created_at` DATETIME NOT NULL DEFAULT NOW(),
  `updated_at` DATETIME NOT NULL DEFAULT NOW() ON UPDATE NOW(),
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_visuals_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_visuals_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `visuals`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
