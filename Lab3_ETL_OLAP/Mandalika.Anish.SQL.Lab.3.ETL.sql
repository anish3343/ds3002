# Anish Mandalika, am8wk@virginia.edu
# DS 3002: Data Science Systems
# Lab 3: ETL and OLAP

#-------------------------------------------------------------------------------------------
# PART 1: CREATE DIMENSIONAL SCHEMA
#-------------------------------------------------------------------------------------------

DROP DATABASE IF EXISTS `northwind_dw`;
CREATE DATABASE `northwind_dw` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

DROP TABLE IF EXISTS `dim_customers`;
CREATE TABLE `dim_customers` (
  `customer_key` int NOT NULL AUTO_INCREMENT,
  `company` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `email_address` varchar(50) DEFAULT NULL,
  `job_title` varchar(50) DEFAULT NULL,
  `business_phone` varchar(25) DEFAULT NULL,
  `home_phone` varchar(25) DEFAULT NULL,
  `mobile_phone` varchar(25) DEFAULT NULL,
  `fax_number` varchar(25) DEFAULT NULL,
  `address` longtext,
  `city` varchar(50) DEFAULT NULL,
  `state_province` varchar(50) DEFAULT NULL,
  `zip_postal_code` varchar(15) DEFAULT NULL,
  `country_region` varchar(50) DEFAULT NULL,
  # `web_page` longtext,
  # `notes` longtext,
  # `attachments` longblob,
  PRIMARY KEY (`customer_key`),
  KEY `city` (`city`),
  KEY `company` (`company`),
  KEY `first_name` (`first_name`),
  KEY `last_name` (`last_name`),
  KEY `zip_postal_code` (`zip_postal_code`),
  KEY `state_province` (`state_province`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `dim_employees`;
CREATE TABLE `dim_employees` (
  `employee_key` int NOT NULL AUTO_INCREMENT,
  `company` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `email_address` varchar(50) DEFAULT NULL,
  `job_title` varchar(50) DEFAULT NULL,
  `business_phone` varchar(25) DEFAULT NULL,
  `home_phone` varchar(25) DEFAULT NULL,
  `mobile_phone` varchar(25) DEFAULT NULL,
  `fax_number` varchar(25) DEFAULT NULL,
  `address` longtext,
  `city` varchar(50) DEFAULT NULL,
  `state_province` varchar(50) DEFAULT NULL,
  `zip_postal_code` varchar(15) DEFAULT NULL,
  `country_region` varchar(50) DEFAULT NULL,
  `web_page` longtext,
  # `notes` longtext,
  # `attachments` longblob,
  PRIMARY KEY (`employee_key`),
  KEY `city` (`city`),
  KEY `company` (`company`),
  KEY `first_name` (`first_name`),
  KEY `last_name` (`last_name`),
  KEY `zip_postal_code` (`zip_postal_code`),
  KEY `state_province` (`state_province`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `dim_products`;
CREATE TABLE `dim_products` (
  # `supplier_ids` longtext,
  `product_key` int NOT NULL AUTO_INCREMENT,
  `product_code` varchar(25) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  # `description` longtext,
  `standard_cost` decimal(19,4) DEFAULT '0.0000',
  `list_price` decimal(19,4) NOT NULL DEFAULT '0.0000',
  `reorder_level` int DEFAULT NULL,
  `target_level` int DEFAULT NULL,
  `quantity_per_unit` varchar(50) DEFAULT NULL,
  `discontinued` tinyint(1) NOT NULL DEFAULT '0',
  `minimum_reorder_quantity` int DEFAULT NULL,
  `category` varchar(50) DEFAULT NULL,
  # `attachments` longblob,
  PRIMARY KEY (`product_key`),
  KEY `product_code` (`product_code`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `dim_shippers`;
CREATE TABLE `dim_shippers` (
  `shipper_key` int NOT NULL AUTO_INCREMENT,
  `company` varchar(50) DEFAULT NULL,
  # `last_name` varchar(50) DEFAULT NULL,
  # `first_name` varchar(50) DEFAULT NULL,
  # `email_address` varchar(50) DEFAULT NULL,
  # `job_title` varchar(50) DEFAULT NULL,
  # `business_phone` varchar(25) DEFAULT NULL,
  # `home_phone` varchar(25) DEFAULT NULL,
  # `mobile_phone` varchar(25) DEFAULT NULL,
  # `fax_number` varchar(25) DEFAULT NULL,
  `address` longtext,
  `city` varchar(50) DEFAULT NULL,
  `state_province` varchar(50) DEFAULT NULL,
  `zip_postal_code` varchar(15) DEFAULT NULL,
  `country_region` varchar(50) DEFAULT NULL,
  # `web_page` longtext,
  # `notes` longtext,
  # `attachments` longblob,
  PRIMARY KEY (`shipper_key`),
  KEY `city` (`city`),
  KEY `company` (`company`),
  # KEY `first_name` (`first_name`),
  # KEY `last_name` (`last_name`),
  KEY `zip_postal_code` (`zip_postal_code`),
  KEY `state_province` (`state_province`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `fact_orders`;
CREATE TABLE `fact_orders`(
  `fact_order_key` int NOT NULL AUTO_INCREMENT,
  `employee_id` int DEFAULT NULL,
  `customer_id` int DEFAULT NULL,
  `order_id` int NOT NULL,
  `product_id` int DEFAULT NULL,
  `order_date` datetime DEFAULT NULL,
  `shipped_date` datetime DEFAULT NULL,
  `shipper_id` int DEFAULT NULL,
  `ship_name` varchar(50) DEFAULT NULL,
  `ship_address` longtext,
  `ship_city` varchar(50) DEFAULT NULL,
  `ship_state_province` varchar(50) DEFAULT NULL,
  `ship_zip_postal_code` varchar(50) DEFAULT NULL,
  `ship_country_region` varchar(50) DEFAULT NULL,
  `shipping_fee` decimal(19,4) DEFAULT '0.0000',
  `taxes` decimal(19,4) DEFAULT '0.0000',
  `payment_type` varchar(50) DEFAULT NULL,
  `paid_date` datetime DEFAULT NULL,
  `tax_rate` double DEFAULT '0',
  `tax_status_id` tinyint DEFAULT NULL,
  `order_status_name` varchar(50) NOT NULL,
  `detail_id` int DEFAULT 0,
  `quantity` decimal(18,4) DEFAULT '0.0000',
  `unit_price` decimal(19,4) DEFAULT '0.0000',
  `discount` double DEFAULT '0',
  `details_status_name` varchar(50),
  `date_allocated` datetime DEFAULT NULL,
  `purchase_order_id` int DEFAULT NULL,
  `inventory_id` int DEFAULT NULL,
  PRIMARY KEY (`fact_order_key`)
)ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8mb4;


#-------------------------------------------------------------------------------------------
# PART 2: POPULATE DIMENSIONAL SCHEMA
#-------------------------------------------------------------------------------------------

INSERT INTO `northwind_dw`.`dim_customers`
(`customer_key`,
`company`,
`last_name`,
`first_name`,
`email_address`,
`job_title`,
`business_phone`,
`home_phone`,
`mobile_phone`,
`fax_number`,
`address`,
`city`,
`state_province`,
`zip_postal_code`,
`country_region`)
SELECT `customers`.`id`,
    `customers`.`company`,
    `customers`.`last_name`,
    `customers`.`first_name`,
    `customers`.`email_address`,
    `customers`.`job_title`,
    `customers`.`business_phone`,
    `customers`.`home_phone`,
    `customers`.`mobile_phone`,
    `customers`.`fax_number`,
    `customers`.`address`,
    `customers`.`city`,
    `customers`.`state_province`,
    `customers`.`zip_postal_code`,
    `customers`.`country_region`
FROM `northwind`.`customers`;

INSERT INTO `northwind_dw`.`dim_employees`
(`employee_key`,
`company`,
`last_name`,
`first_name`,
`email_address`,
`job_title`,
`business_phone`,
`home_phone`,
`mobile_phone`,
`fax_number`,
`address`,
`city`,
`state_province`,
`zip_postal_code`,
`country_region`,
`web_page`)
SELECT `employees`.`id`,
    `employees`.`company`,
    `employees`.`last_name`,
    `employees`.`first_name`,
    `employees`.`email_address`,
    `employees`.`job_title`,
    `employees`.`business_phone`,
    `employees`.`home_phone`,
    `employees`.`mobile_phone`,
    `employees`.`fax_number`,
    `employees`.`address`,
    `employees`.`city`,
    `employees`.`state_province`,
    `employees`.`zip_postal_code`,
    `employees`.`country_region`,
    `employees`.`web_page`
FROM `northwind`.`employees`;

INSERT INTO `northwind_dw`.`dim_products`
(`product_key`,
`product_code`,
`product_name`,
`standard_cost`,
`list_price`,
`reorder_level`,
`target_level`,
`quantity_per_unit`,
`discontinued`,
`minimum_reorder_quantity`,
`category`)
SELECT `products`.`id`,
    `products`.`product_code`,
    `products`.`product_name`,
    `products`.`standard_cost`,
    `products`.`list_price`,
    `products`.`reorder_level`,
    `products`.`target_level`,
    `products`.`quantity_per_unit`,
    `products`.`discontinued`,
    `products`.`minimum_reorder_quantity`,
    `products`.`category`
FROM `northwind`.`products`;

INSERT INTO `northwind_dw`.`dim_shippers`
(`shipper_key`,
`company`,
`address`,
`city`,
`state_province`,
`zip_postal_code`,
`country_region`)
SELECT `shippers`.`id`,
    `shippers`.`company`,
    `shippers`.`address`,
    `shippers`.`city`,
    `shippers`.`state_province`,
    `shippers`.`zip_postal_code`,
    `shippers`.`country_region`
FROM `northwind`.`shippers`;

INSERT INTO `northwind_dw`.`fact_orders`
(`employee_id`,
`customer_id`,
`order_id`,
`product_id`,
`order_date`,
`shipped_date`,
`shipper_id`,
`ship_name`,
`ship_address`,
`ship_city`,
`ship_state_province`,
`ship_zip_postal_code`,
`ship_country_region`,
`shipping_fee`,
`taxes`,
`payment_type`,
`paid_date`,
`tax_rate`,
`tax_status_id`,
`order_status_name`,
`detail_id`,
`quantity`,
`unit_price`,
`discount`,
`details_status_name`,
`date_allocated`,
`purchase_order_id`,
`inventory_id`)
SELECT `orders`.`employee_id`,
    `orders`.`customer_id`,
    `orders`.`id`,
    `order_details`.`product_id`,
    `orders`.`order_date`,
    `orders`.`shipped_date`,
    `orders`.`shipper_id`,
    `orders`.`ship_name`,
    `orders`.`ship_address`,
    `orders`.`ship_city`,
    `orders`.`ship_state_province`,
    `orders`.`ship_zip_postal_code`,
    `orders`.`ship_country_region`,
    `orders`.`shipping_fee`,
    `orders`.`taxes`,
    `orders`.`payment_type`,
    `orders`.`paid_date`,
    `orders`.`tax_rate`,
    `orders`.`tax_status_id`,
    `orders_status`.`status_name`,
    `order_details`.`id`,
    `order_details`.`quantity`,
    `order_details`.`unit_price`,
    `order_details`.`discount`,
    `order_details_status`.`status_name`,
    `order_details`.`date_allocated`,
    `order_details`.`purchase_order_id`,
    `order_details`.`inventory_id`    
FROM `northwind`.`orders`
LEFT JOIN `northwind`.`orders_status`
ON `northwind`.`orders_status`.`id` = `northwind`.`orders`.`status_id`
LEFT JOIN `northwind`.`order_details`
ON `northwind`.`orders`.`id` = `northwind`.`order_details`.`order_id`
LEFT JOIN `northwind`.`order_details_status`
ON `northwind`.`order_details`.`status_id` = `northwind`.`order_details_status`.`id`;

#-------------------------------------------------------------------------------------------
# PART 3: DIMENSIONAL REPORT
#-------------------------------------------------------------------------------------------

SELECT `dim_customers`.`last_name` AS `customer_name`,
	SUM(`fact_orders`.`quantity`) AS `total_quantity`,
    SUM(`fact_orders`.`unit_price`) AS `total_unit_price`
FROM `northwind_dw`.`fact_orders`
LEFT JOIN `northwind_dw`.`dim_customers`
ON `dim_customers`.`customer_key` = `fact_orders`.`customer_id`
GROUP BY `dim_customers`.`last_name`;