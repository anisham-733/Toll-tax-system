-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2022 at 05:51 PM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tolltaxdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `taxfare`
--

CREATE TABLE `taxfare` (
  `id` int(11) NOT NULL,
  `vehicle_category` varchar(255) NOT NULL,
  `Single` double NOT NULL,
  `Return_tax` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `taxfare`
--

INSERT INTO `taxfare` (`id`, `vehicle_category`, `Single`, `Return_tax`) VALUES
(201, 'Car/Jeep/Van', 90, 135),
(202, 'Light Commercial vehicles', 150, 220),
(203, 'Bus/Truck', 318, 465),
(204, '3-axle vehicles', 335, 505),
(205, '4 to 6 axle vehicles', 485, 730),
(206, 'Heavy vehicles', 490, 730),
(207, '7 or more axle vehicles', 590, 885);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `taxfare`
--
ALTER TABLE `taxfare`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `taxfare`
--
ALTER TABLE `taxfare`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=208;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
