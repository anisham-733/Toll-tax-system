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
-- Table structure for table `tollplaza`
--

CREATE TABLE `tollplaza` (
  `tollid` int(11) NOT NULL,
  `toll_name` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `state` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tollplaza`
--

INSERT INTO `tollplaza` (`tollid`, `toll_name`, `password`, `city`, `state`, `email`) VALUES
(101, 'Delhibooth', 'SNmulsGy', 'Chandigarh', 'Punjab', 'anisha.amcse@gmail.com'),
(1002, 'L&T Vadodra', 'lZYLKtMa', 'Vadodara', 'Gujarat', 'anisha.amcse@gmail.com'),
(1100, 'Amritsar Toll', 'JQu5DWnQ', 'Amritsar', 'Punjab', '19001mittalr@gmail.com'),
(2005, 'Ahmedabad Toll Plaza', 'SIkBd0MI', 'Ahmedabad', 'Gujarat', 'anisha.amcse@gmail.com'),
(13200, 'Udaipur Kherwara', '35mj4Ebj', 'Jaipur', 'Rajasthan', 'anisha.amcse@gmail.com'),
(14001, 'Ambala Chandigarh', 'FDwpVDfz', 'Sahibzada Ajit Singh Nagar', 'Punjab', 'tollchd@gmail.com'),
(39001, 'L&T PANIPAT', 'hKPKpbQ2', 'Panipat', 'Haryana', '895_panipat@gmail.com'),
(41001, 'JATL Dhilwan Toll Plaza', '2xlIBJKK', 'Kapurthala', 'Pujabi', '90dhiwan@gmail.com'),
(154001, 'Gharonda Toll Plaza', 'IRs77tdJ', 'Karnal', 'Haryana', '125gharonda@gmail.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tollplaza`
--
ALTER TABLE `tollplaza`
  ADD PRIMARY KEY (`tollid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
