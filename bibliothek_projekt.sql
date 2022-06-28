-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 01. Jun 2022 um 11:23
-- Server-Version: 10.4.21-MariaDB
-- PHP-Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `bibliothek_projekt`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `ausleihe`
--

CREATE TABLE `ausleihe` (
  `Entleihe` int(11) NOT NULL,
  `Frist` int(11) NOT NULL,
  `AusweisID` int(11) NOT NULL,
  `BuchID` int(11) NOT NULL,
  `Rückgabe` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `autor`
--

CREATE TABLE `autor` (
  `AutorID` int(11) NOT NULL,
  `Vorname` varchar(45) NOT NULL,
  `Nachname` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `bibliotheksbenutzer`
--

CREATE TABLE `bibliotheksbenutzer` (
  `AusweisID` int(11) NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Nachname` varchar(45) NOT NULL,
  `Straße` varchar(45) NOT NULL,
  `PLZ` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `buch`
--

CREATE TABLE `buch` (
  `ISBN` int(11) NOT NULL,
  `VerlagID` int(11) NOT NULL,
  `Titel` varchar(45) NOT NULL,
  `Kategorie` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `bücher`
--

CREATE TABLE `bücher` (
  `BücherID` int(11) NOT NULL,
  `ISBN` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `identifikation`
--

CREATE TABLE `identifikation` (
  `AutorID` int(11) NOT NULL,
  `ISBN` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `verlag`
--

CREATE TABLE `verlag` (
  `VerlagID` int(11) NOT NULL,
  `Telefonnummer` varchar(45) DEFAULT NULL,
  `Straße` varchar(45) NOT NULL,
  `PLZ` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `ausleihe`
--
ALTER TABLE `ausleihe`
  ADD PRIMARY KEY (`Entleihe`);

--
-- Indizes für die Tabelle `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`AutorID`);

--
-- Indizes für die Tabelle `bibliotheksbenutzer`
--
ALTER TABLE `bibliotheksbenutzer`
  ADD PRIMARY KEY (`AusweisID`);

--
-- Indizes für die Tabelle `buch`
--
ALTER TABLE `buch`
  ADD PRIMARY KEY (`ISBN`);

--
-- Indizes für die Tabelle `bücher`
--
ALTER TABLE `bücher`
  ADD PRIMARY KEY (`BücherID`);

--
-- Indizes für die Tabelle `identifikation`
--
ALTER TABLE `identifikation`
  ADD PRIMARY KEY (`AutorID`);

--
-- Indizes für die Tabelle `verlag`
--
ALTER TABLE `verlag`
  ADD PRIMARY KEY (`VerlagID`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `ausleihe`
--
ALTER TABLE `ausleihe`
  MODIFY `Entleihe` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `autor`
--
ALTER TABLE `autor`
  MODIFY `AutorID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `bibliotheksbenutzer`
--
ALTER TABLE `bibliotheksbenutzer`
  MODIFY `AusweisID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `buch`
--
ALTER TABLE `buch`
  MODIFY `ISBN` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `bücher`
--
ALTER TABLE `bücher`
  MODIFY `BücherID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT für Tabelle `verlag`
--
ALTER TABLE `verlag`
  MODIFY `VerlagID` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
