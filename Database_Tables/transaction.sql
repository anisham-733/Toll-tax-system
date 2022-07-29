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
-- Table structure for table `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `vehicle_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(255) NOT NULL,
  `vehicle_category` varchar(255) NOT NULL,
  `fare` double NOT NULL,
  `toll_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`id`, `vehicle_id`, `date`, `time`, `vehicle_category`, `fare`, `toll_id`) VALUES
(22, 10262, '2021-11-30', ' 08:01:20', 'Car/Jeep/Van', 90, 1002),
(23, 10263, '2021-11-30', ' 08:08:24', 'Car/Jeep/Van', 135, 1002),
(24, 10258, '2021-11-30', ' 08:10:27', 'Light Commercial vehicles', 220, 1002),
(25, 10258, '2021-12-01', ' 10:09:42', 'Light Commercial vehicles', 220, 1100),
(26, 10258, '2021-12-01', ' 10:09:42', 'Light Commercial vehicles', 220, 1100),
(27, 10258, '2021-12-01', ' 10:13:11', 'Light Commercial vehicles', 220, 1100),
(28, 10258, '2021-12-01', ' 10:16:20', 'Light Commercial vehicles', 220, 1100),
(30, 10262, '2021-12-01', ' 10:28:03', 'Car/Jeep/Van', 90, 1100),
(32, 10262, '2021-12-01', ' 01:34:00', 'Car/Jeep/Van', 90, 1002),
(33, 10258, '2021-12-01', ' 02:15:27', 'Light Commercial vehicles', 220, 1002),
(34, 10263, '2022-01-05', ' 01:41:19', 'Car/Jeep/Van', 135, 1002),
(35, 10263, '2022-02-03', ' 09:28:42', 'Car/Jeep/Van', 135, 1002),
(36, 10262, '2022-02-03', ' 11:41:21', 'Car/Jeep/Van', 90, 101),
(37, 10258, '2022-04-16', ' 01:18:36', 'Light Commercial vehicles', 220, 1002),
(38, 10262, '2022-04-16', ' 01:34:24', 'Car/Jeep/Van', 90, 1002),
(39, 10258, '2022-04-16', ' 01:48:15', 'Light Commercial vehicles', 220, 1002);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `vehicle_id` (`vehicle_id`),
  ADD KEY `toll_id` (`toll_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `transaction`
--
ALTER TABLE `transaction`
  ADD CONSTRAINT `transaction_ibfk_1` FOREIGN KEY (`vehicle_id`) REFERENCES `vehicle_reg` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `transaction_ibfk_2` FOREIGN KEY (`toll_id`) REFERENCES `tollplaza` (`tollid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
