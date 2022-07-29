-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2022 at 05:50 PM
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
-- Table structure for table `issuemonthlypass`
--

CREATE TABLE `issuemonthlypass` (
  `id` int(255) NOT NULL,
  `vehicleid` int(255) NOT NULL,
  `passid` int(255) NOT NULL,
  `date_of_issue` date NOT NULL,
  `expirydate` date NOT NULL,
  `fare_type` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issuemonthlypass`
--

INSERT INTO `issuemonthlypass` (`id`, `vehicleid`, `passid`, `date_of_issue`, `expirydate`, `fare_type`) VALUES
(352, 10261, 303, '2021-12-01', '2021-12-31', 'Prepaid');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `issuemonthlypass`
--
ALTER TABLE `issuemonthlypass`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vehicleid` (`vehicleid`),
  ADD KEY `passid` (`passid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `issuemonthlypass`
--
ALTER TABLE `issuemonthlypass`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=353;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `issuemonthlypass`
--
ALTER TABLE `issuemonthlypass`
  ADD CONSTRAINT `issuemonthlypass_ibfk_1` FOREIGN KEY (`vehicleid`) REFERENCES `vehicle_reg` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `issuemonthlypass_ibfk_2` FOREIGN KEY (`passid`) REFERENCES `monthlypass` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
