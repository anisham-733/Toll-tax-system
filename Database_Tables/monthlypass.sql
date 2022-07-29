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
-- Table structure for table `monthlypass`
--

CREATE TABLE `monthlypass` (
  `id` int(11) NOT NULL,
  `vehicle_category` varchar(255) NOT NULL,
  `monthly_pass` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `monthlypass`
--

INSERT INTO `monthlypass` (`id`, `vehicle_category`, `monthly_pass`) VALUES
(301, 'Car/Jeep/Van', 3045),
(302, 'Light Commercial vehicles', 4920),
(303, 'Bus/Truck', 10310),
(304, '3-axle vehicles', 11250),
(305, '4 to 6 axle vehicles', 16170),
(306, 'Heavy vehicles', 16170),
(307, '7 or more axle vehicles', 19690);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `monthlypass`
--
ALTER TABLE `monthlypass`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `monthlypass`
--
ALTER TABLE `monthlypass`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=308;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
