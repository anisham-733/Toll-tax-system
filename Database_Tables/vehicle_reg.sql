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
-- Table structure for table `vehicle_reg`
--

CREATE TABLE `vehicle_reg` (
  `id` int(11) NOT NULL,
  `vehicle_no` varchar(255) NOT NULL,
  `ownername` varchar(255) NOT NULL,
  `vehicle_category` varchar(255) NOT NULL,
  `journey_type` varchar(255) NOT NULL,
  `tax_type` varchar(255) NOT NULL,
  `contactno` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_reg`
--

INSERT INTO `vehicle_reg` (`id`, `vehicle_no`, `ownername`, `vehicle_category`, `journey_type`, `tax_type`, `contactno`) VALUES
(10251, 'MH2EE7598', 'Anisha Mahajan', 'Car/Jeep/Van', 'Return', 'Prepaid', '9877463071'),
(10252, 'PBO2DY7999', 'Anmol Chawla', 'Car/Jeep/Van', 'Single', 'Prepaid', '8146077944'),
(10254, 'PB02AP4474', 'Rajkumar Mahajan', 'Car/Jeep/Van', 'Return', 'Prepaid', '9877662885'),
(10258, 'DL8CAF5030', 'Anisha Mahajan', 'Light Commercial vehicles', 'Return', 'Postpaid', '8146077944'),
(10261, 'CG07CA5233', 'Surinder Singh', 'Car/Jeep/Van', 'Monthly Pass', 'Postpaid', '8146077944'),
(10262, 'MH20EE7598', 'Kartik ', 'Car/Jeep/Van', 'Single', 'Prepaid', '9877463071'),
(10263, 'KL26H5009', 'Danvi Sharma', 'Car/Jeep/Van', 'Return', 'Postpaid', '8146077944');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `vehicle_reg`
--
ALTER TABLE `vehicle_reg`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `vehicle_reg`
--
ALTER TABLE `vehicle_reg`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10265;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
