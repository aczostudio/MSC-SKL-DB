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

-- Dumping data for table msc-skl_db.clerk: ~0 rows (approximately)
/*!40000 ALTER TABLE `clerk` DISABLE KEYS */;
/*!40000 ALTER TABLE `clerk` ENABLE KEYS */;

-- Dumping data for table msc-skl_db.company: ~0 rows (approximately)
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
REPLACE INTO `company` (`CompanyName`, `CompanyOwner`, `CompanyAddress`, `CompanyContactInfo`, `CompanyTaxID`) VALUES
	('Marine Survitec Songkhla Co.,Ltd.', 'Wanna Tanratanawong', '182/2 Sating-Mo Singhanakorn Songkhla 90280 Thailand', 'Tel.080-456-8001 Email:msc.songkhla@gmail.com', '000000000000');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;

-- Dumping data for table msc-skl_db.customer: ~4 rows (approximately)
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
REPLACE INTO `customer` (`CustomerName`, `CustomerAddress`, `CustomerContactInfo`, `CustomerTaxID`) VALUES
	('Clearvac Engineering Asia Co.,Ltd. (Head office)', '20/78 หมู่2 ต.เกาะแก้ว อ.เมือง จังหวัดภูเก็ต 83000', '093-580-2588', '0835560008357'),
	('S.J GLOBAL TRADE.,LTD PART.', '87 Chotivittayakul4 Road, Hatyai Songkhla 90110', '074-559-426 , 086-481-3478', NULL),
	('บริษัท ซิลเวอร์ไลนิ่ง ภูเก็ต จำกัด(Head office)', '23/92 หมู่2 ต.เกาะแก้ว อ.เมือง จังหวัดภูเก็ต 83000', '000-0000', NULL),
	('บริษัท แกรนด์ไลออน จำกัด', '96 ถ.สวนสิริ ต.หาดใหญ่ อ.หาดใหญ่ จ.สงขลา 90110', '081-896-6017 info@gr.go.th', '0905554002180');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;

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

-- Dumping data for table msc-skl_db.employee: ~0 rows (approximately)
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;

-- Dumping data for table msc-skl_db.product: ~5 rows (approximately)
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
REPLACE INTO `product` (`ProductName`, `ProductDescription`, `ProductPrice`, `ProductUnit`, `ProductAmount`) VALUES
	('BA-CYLN-HWAYAN', 'BA Cylinder brand Hwayan', 10000, 'Cyln', 4),
	('BA-CYLN-RONGUI', 'Ba Cylinder brand Rongui', 10000, 'Cyln', 15),
	('FE-AF-20L', 'Foam AFFF 3% Size:20Ltrs.', 5500, 'Pcs', 5),
	('FE-AF-6.0', 'Portable Foam AFFF Size:6.0Ltrs', 3000, 'Cyln', 1),
	('TS-PRODUCT', 'Test Producct', 999, 'Test', 99);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;

-- Dumping data for table msc-skl_db.quotation: ~2 rows (approximately)
/*!40000 ALTER TABLE `quotation` DISABLE KEYS */;
REPLACE INTO `quotation` (`QuotationID`, `QuotationDate`, `QuotationTotalPrice`, `QuotationVatPrice`, `QuotationNetTotal`, `CustomerProductOrderID`) VALUES
	('quo20010003', '2020-01-27', 11111, 111, 11222, 'quo20010003'),
	('quo20010004', '2020-01-28', 26500, 700, 27200, 'quo20010004');
/*!40000 ALTER TABLE `quotation` ENABLE KEYS */;

-- Dumping data for table msc-skl_db.tools: ~0 rows (approximately)
/*!40000 ALTER TABLE `tools` DISABLE KEYS */;
/*!40000 ALTER TABLE `tools` ENABLE KEYS */;

-- Dumping data for table msc-skl_db.toolsrequisition: ~0 rows (approximately)
/*!40000 ALTER TABLE `toolsrequisition` DISABLE KEYS */;
/*!40000 ALTER TABLE `toolsrequisition` ENABLE KEYS */;

-- Dumping data for table msc-skl_db.vesselorrig: ~0 rows (approximately)
/*!40000 ALTER TABLE `vesselorrig` DISABLE KEYS */;
/*!40000 ALTER TABLE `vesselorrig` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
