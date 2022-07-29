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
-- Table structure for table `entry`
--

CREATE TABLE `entry` (
  `id` int(11) NOT NULL,
  `vehicleid` int(11) NOT NULL,
  `entry_time` varchar(255) NOT NULL,
  `entry_date` date NOT NULL,
  `entry_type` varchar(255) NOT NULL,
  `toll_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `entry`
--

INSERT INTO `entry` (`id`, `vehicleid`, `entry_time`, `entry_date`, `entry_type`, `toll_id`) VALUES
(19606, 10262, ' 08:01:20', '2021-11-30', 'Single', 1002),
(19607, 10263, ' 08:08:24', '2021-11-30', 'Return', 1002),
(19608, 10258, ' 08:10:27', '2021-11-30', 'Return', 1002),
(19609, 10258, ' 10:09:42', '2021-12-01', 'Return', 1100),
(19610, 10258, ' 10:09:42', '2021-12-01', 'Return', 1100),
(19611, 10258, ' 10:13:11', '2021-12-01', 'Return', 1100),
(19612, 10258, ' 10:16:20', '2021-12-01', 'Return', 1100),
(19614, 10262, ' 10:28:03', '2021-12-01', 'Single', 1100),
(19616, 10262, ' 01:34:00', '2021-12-01', 'Single', 1002),
(19617, 10258, ' 02:15:27', '2021-12-01', 'Return', 1002),
(19618, 10263, ' 01:41:19', '2022-01-05', 'Return', 1002),
(19619, 10263, ' 09:28:42', '2022-02-03', 'Return', 1002),
(19620, 10262, ' 11:41:21', '2022-02-03', 'Single', 101),
(19621, 10258, ' 01:18:36', '2022-04-16', 'Return', 1002),
(19622, 10262, ' 01:34:24', '2022-04-16', 'Single', 1002),
(19623, 10258, ' 01:48:15', '2022-04-16', 'Return', 1002);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `entry`
--
ALTER TABLE `entry`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vid` (`vehicleid`),
  ADD KEY `toll_id` (`toll_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `entry`
--
ALTER TABLE `entry`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19624;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `entry`
--
ALTER TABLE `entry`
  ADD CONSTRAINT `entry_ibfk_1` FOREIGN KEY (`toll_id`) REFERENCES `tollplaza` (`tollid`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `vid` FOREIGN KEY (`vehicleid`) REFERENCES `vehicle_reg` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
