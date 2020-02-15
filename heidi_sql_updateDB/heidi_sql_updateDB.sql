-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               10.4.12-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             10.3.0.5876
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for msc-skl_db
CREATE DATABASE IF NOT EXISTS `msc-skl_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `msc-skl_db`;

-- Dumping structure for table msc-skl_db.clerk
CREATE TABLE IF NOT EXISTS `clerk` (
  `ClerkID` varchar(50) NOT NULL DEFAULT '',
  `ClerkDepartment` varchar(50) DEFAULT '',
  `EmployeeName` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`ClerkID`),
  KEY `Index 2` (`EmployeeName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Company''s adminstration officer.';

-- Dumping data for table msc-skl_db.clerk: ~0 rows (approximately)
/*!40000 ALTER TABLE `clerk` DISABLE KEYS */;
/*!40000 ALTER TABLE `clerk` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.company
CREATE TABLE IF NOT EXISTS `company` (
  `CompanyName` varchar(50) NOT NULL,
  `CompanyOwner` varchar(50) DEFAULT NULL,
  `CompanyAddress` varchar(200) DEFAULT NULL,
  `CompanyContactInfo` varchar(100) DEFAULT NULL,
  `CompanyTaxID` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`CompanyName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Company detail';

-- Dumping data for table msc-skl_db.company: ~0 rows (approximately)
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
REPLACE INTO `company` (`CompanyName`, `CompanyOwner`, `CompanyAddress`, `CompanyContactInfo`, `CompanyTaxID`) VALUES
	('Marine Survitec Songkhla Co.,Ltd.', 'Wanna Tanratanawong', '182/2 Sating-Mo Singhanakorn Songkhla 90280 Thailand', 'Tel.080-456-8001 Email:msc.songkhla@gmail.com', '000000000000');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.customer
CREATE TABLE IF NOT EXISTS `customer` (
  `CustomerName` varchar(50) NOT NULL,
  `CustomerAddress` varchar(200) DEFAULT NULL,
  `CustomerContactInfo` varchar(100) DEFAULT NULL,
  `CustomerTaxID` varchar(13) DEFAULT NULL,
  PRIMARY KEY (`CustomerName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Customer''s table';

-- Dumping data for table msc-skl_db.customer: ~4 rows (approximately)
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
REPLACE INTO `customer` (`CustomerName`, `CustomerAddress`, `CustomerContactInfo`, `CustomerTaxID`) VALUES
	('Clearvac Engineering Asia Co.,Ltd. (Head office)', '20/78 หมู่2 ต.เกาะแก้ว อ.เมือง จังหวัดภูเก็ต 83000', '093-580-2588', '0835560008357'),
	('S.J GLOBAL TRADE.,LTD PART.', '87 Chotivittayakul4 Road, Hatyai Songkhla 90110', '074-559-426 , 086-481-3478', NULL),
	('บริษัท ซิลเวอร์ไลนิ่ง ภูเก็ต จำกัด(Head office)', '23/92 หมู่2 ต.เกาะแก้ว อ.เมือง จังหวัดภูเก็ต 83000', '000-0000', NULL),
	('บริษัท แกรนด์ไลออน จำกัด', '96 ถ.สวนสิริ ต.หาดใหญ่ อ.หาดใหญ่ จ.สงขลา 90110', '081-896-6017 info@gr.go.th', '0905554002180');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.customerproductorder
CREATE TABLE IF NOT EXISTS `customerproductorder` (
  `CustomerProductOrderID` varchar(50) NOT NULL DEFAULT '',
  `CustomerProductOrderDate` date NOT NULL DEFAULT curdate(),
  `ProductName` varchar(50) NOT NULL DEFAULT '',
  `CustomerProductOrderQuantity` smallint(6) DEFAULT NULL,
  `CustomerProductOrderVat` float DEFAULT NULL,
  `ClerkID` varchar(50) NOT NULL DEFAULT '',
  `CustomerName` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`CustomerProductOrderID`,`ProductName`),
  KEY `FK_customerproductorder_product` (`ProductName`),
  CONSTRAINT `FK_customerproductorder_product` FOREIGN KEY (`ProductName`) REFERENCES `product` (`ProductName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Customer''s product order';

-- Dumping data for table msc-skl_db.customerproductorder: ~6 rows (approximately)
/*!40000 ALTER TABLE `customerproductorder` DISABLE KEYS */;
REPLACE INTO `customerproductorder` (`CustomerProductOrderID`, `CustomerProductOrderDate`, `ProductName`, `CustomerProductOrderQuantity`, `CustomerProductOrderVat`, `ClerkID`, `CustomerName`) VALUES
	('quo20010002', '2020-01-28', 'BA-CYLN-HWAYAN', 1, 0.07, 'clerk_dummy', 'msit'),
	('quo20010002', '2020-01-28', 'FE-AF-20L', 3, 0, 'clerk_dummy', 'msit'),
	('quo20010003', '2020-01-28', 'BA-CYLN-HWAYAN', 1, 0.07, 'clerk_dummy', 'msit'),
	('quo20010003', '2020-01-28', 'FE-AF-20L', 3, 0, 'clerk_dummy', 'msit'),
	('quo20010004', '2020-01-28', 'BA-CYLN-HWAYAN', 1, 0.07, 'clerk_dummy', 'msit'),
	('quo20010004', '2020-01-28', 'FE-AF-20L', 3, 0, 'clerk_dummy', 'msit');
/*!40000 ALTER TABLE `customerproductorder` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.employee
CREATE TABLE IF NOT EXISTS `employee` (
  `EmployeeName` varchar(70) NOT NULL,
  `EmployeeContactInfo` varchar(100) DEFAULT NULL,
  `EmployeeAddress` varchar(200) DEFAULT NULL,
  `EmployeeDepartment` varchar(50) DEFAULT NULL,
  `CompanyName` varchar(50) NOT NULL,
  PRIMARY KEY (`EmployeeName`),
  KEY `FORIEGN KEY` (`CompanyName`),
  CONSTRAINT `FK_employee_company` FOREIGN KEY (`CompanyName`) REFERENCES `company` (`CompanyName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Employee detail';

-- Dumping data for table msc-skl_db.employee: ~0 rows (approximately)
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.product
CREATE TABLE IF NOT EXISTS `product` (
  `ProductName` varchar(50) NOT NULL,
  `ProductDescription` varchar(50) DEFAULT NULL,
  `ProductPrice` mediumint(9) DEFAULT 0,
  `ProductUnit` varchar(50) DEFAULT NULL,
  `ProductAmount` mediumint(9) DEFAULT 0,
  PRIMARY KEY (`ProductName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Product sell in company';

-- Dumping data for table msc-skl_db.product: ~5 rows (approximately)
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
REPLACE INTO `product` (`ProductName`, `ProductDescription`, `ProductPrice`, `ProductUnit`, `ProductAmount`) VALUES
	('BA-CYLN-HWAYAN', 'BA Cylinder brand Hwayan', 10000, 'Cyln', 4),
	('BA-CYLN-RONGUI', 'Ba Cylinder brand Rongui', 10000, 'Cyln', 15),
	('FE-AF-20L', 'Foam AFFF 3% Size:20Ltrs.', 5500, 'Pcs', 5),
	('FE-AF-6.0', 'Portable Foam AFFF Size:6.0Ltrs', 3000, 'Cyln', 1),
	('TS-PRODUCT', 'Test Producct', 999, 'Test', 99);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.quotation
CREATE TABLE IF NOT EXISTS `quotation` (
  `QuotationID` varchar(50) NOT NULL DEFAULT '',
  `QuotationDate` date DEFAULT NULL,
  `QuotationTotalPrice` float DEFAULT NULL,
  `QuotationVatPrice` float DEFAULT NULL,
  `QuotationNetTotal` float DEFAULT NULL,
  `CustomerProductOrderID` varchar(50) NOT NULL DEFAULT '',
  PRIMARY KEY (`QuotationID`),
  KEY `FK_quotation_customerproductorder` (`CustomerProductOrderID`),
  CONSTRAINT `FK_quotation_customerproductorder` FOREIGN KEY (`CustomerProductOrderID`) REFERENCES `customerproductorder` (`CustomerProductOrderID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Company''s quotation with customer order detail';

-- Dumping data for table msc-skl_db.quotation: ~2 rows (approximately)
/*!40000 ALTER TABLE `quotation` DISABLE KEYS */;
REPLACE INTO `quotation` (`QuotationID`, `QuotationDate`, `QuotationTotalPrice`, `QuotationVatPrice`, `QuotationNetTotal`, `CustomerProductOrderID`) VALUES
	('quo20010003', '2020-01-27', 11111, 111, 11222, 'quo20010003'),
	('quo20010004', '2020-01-28', 26500, 700, 27200, 'quo20010004');
/*!40000 ALTER TABLE `quotation` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.tools
CREATE TABLE IF NOT EXISTS `tools` (
  `ToolsName` varchar(50) NOT NULL,
  `ToolsDescription` varchar(100) DEFAULT NULL,
  `ToolsCategory` varchar(30) DEFAULT NULL,
  `ToolsQuantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`ToolsName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tools''s information';

-- Dumping data for table msc-skl_db.tools: ~0 rows (approximately)
/*!40000 ALTER TABLE `tools` DISABLE KEYS */;
/*!40000 ALTER TABLE `tools` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.toolsrequisition
CREATE TABLE IF NOT EXISTS `toolsrequisition` (
  `ToolsRequisitionID` varchar(15) NOT NULL,
  `ToolsRequisitionQuantity` smallint(6) DEFAULT 0,
  `ToolsRequisitionDate` date DEFAULT NULL,
  `TechnicianID` varchar(50) NOT NULL,
  PRIMARY KEY (`ToolsRequisitionID`),
  KEY `FOREIGN KEY` (`TechnicianID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Tools requisition''s information';

-- Dumping data for table msc-skl_db.toolsrequisition: ~0 rows (approximately)
/*!40000 ALTER TABLE `toolsrequisition` DISABLE KEYS */;
/*!40000 ALTER TABLE `toolsrequisition` ENABLE KEYS */;

-- Dumping structure for table msc-skl_db.vesselorrig
CREATE TABLE IF NOT EXISTS `vesselorrig` (
  `VesselOrRigName` varchar(50) NOT NULL,
  `VesselOrRigDescription` varchar(100) DEFAULT NULL,
  `VesselOrRigIMONumber` varchar(20) DEFAULT NULL,
  `VesselOrRigClassify` varchar(30) DEFAULT NULL,
  `VesselOrRigFlagship` varchar(30) DEFAULT NULL,
  `VesselOrRigType` varchar(40) DEFAULT NULL,
  `CustomerName` varchar(50) NOT NULL,
  PRIMARY KEY (`VesselOrRigName`),
  KEY `FORIEGN KEY` (`CustomerName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='Customer''s vessel or rig information';

-- Dumping data for table msc-skl_db.vesselorrig: ~0 rows (approximately)
/*!40000 ALTER TABLE `vesselorrig` DISABLE KEYS */;
/*!40000 ALTER TABLE `vesselorrig` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
