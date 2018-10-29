/*
Navicat MySQL Data Transfer

Source Server         : bleww_01
Source Server Version : 50624
Source Host           : www.bleww.com:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50624
File Encoding         : 65001

Date: 2017-03-02 15:24:21
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `Dept`
-- ----------------------------
DROP TABLE IF EXISTS `Dept`;
CREATE TABLE `Dept` (
  `Dept_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Remark` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`Dept_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Dept
-- ----------------------------
INSERT INTO `Dept` VALUES ('1', '上海销售部门', null);
INSERT INTO `Dept` VALUES ('2', '北京销售部门', null);
INSERT INTO `Dept` VALUES ('3', '广州销售部门', null);

-- ----------------------------
-- Table structure for `Employee`
-- ----------------------------
DROP TABLE IF EXISTS `Employee`;
CREATE TABLE `Employee` (
  `Employee_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Dept_ID` int(11) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Duty` varchar(20) DEFAULT NULL,
  `Gender` varchar(6) DEFAULT NULL,
  `BirthDate` datetime DEFAULT NULL,
  `HireDate` datetime DEFAULT NULL,
  `MatureDate ` datetime DEFAULT NULL,
  `IdentityCard` varchar(20) DEFAULT NULL,
  `Address` varchar(250) DEFAULT NULL,
  `Phone` varchar(25) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`Employee_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Employee
-- ----------------------------
INSERT INTO `Employee` VALUES ('1', '1', '王晓明', '销售', '男', null, null, null, null, null, null, null);
INSERT INTO `Employee` VALUES ('2', '1', '张方娟', '销售', '女', null, null, null, null, null, null, null);
INSERT INTO `Employee` VALUES ('3', '1', '许建华', '销售', '男', null, null, null, null, null, null, null);
INSERT INTO `Employee` VALUES ('4', '2', '黄月月', '销售', '女', null, null, null, null, null, null, null);
INSERT INTO `Employee` VALUES ('5', '2', '许明辉', '销售经理', '男', null, null, null, null, null, null, null);
INSERT INTO `Employee` VALUES ('6', '3', '李丽丽', '销售', '女', null, null, null, null, null, null, null);

-- ----------------------------
-- Table structure for `Product`
-- ----------------------------
DROP TABLE IF EXISTS `Product`;
CREATE TABLE `Product` (
  `Product_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '/* 商品名称编号, 主键 */',
  `Name` varchar(30) NOT NULL COMMENT '/* 商品名称 */',
  `Price` double NOT NULL COMMENT '/* 参考价格 */',
  `ProductList_ID` int(11) DEFAULT NULL COMMENT '/* 商品细分类编号, 外键 ( 参照 PRODUCTLIST 表 ) */',
  `ProductSpec_ID` int(11) DEFAULT NULL,
  `ProductUnit_ID` int(11) DEFAULT NULL,
  `Employee_ID` int(11) DEFAULT NULL COMMENT '/* 操作员,   外键 ( 参照 EMPLOYEE 表 )*/',
  `CreateDate` datetime DEFAULT NULL,
  `Remark` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of Product
-- ----------------------------
INSERT INTO `Product` VALUES ('1', '笔记本电脑联想E450C', '5000', null, null, null, null, null, null);
INSERT INTO `Product` VALUES ('2', '笔记本电脑联想A420', '3000', null, null, null, null, null, null);
INSERT INTO `Product` VALUES ('3', '红色玫瑰花一束', '50', null, null, null, null, null, null);
INSERT INTO `Product` VALUES ('4', '蓝色玫瑰花一束', '88', null, null, null, null, null, null);
INSERT INTO `Product` VALUES ('5', '紫色玫瑰花一只', '127', null, null, null, null, null, null);

-- ----------------------------
-- Table structure for `Sale`
-- ----------------------------
DROP TABLE IF EXISTS `Sale`;
CREATE TABLE `Sale` (
  `Sale_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '/* 销售 编号  */ ',
  `SaleDate` datetime NOT NULL COMMENT '/* 销售 日期 */',
  `Employee_ID` int(11) NOT NULL COMMENT '/* 售货人,   外键 ( 参照 EMPLOYEE 表)*/',
  `Dept_ID` int(11) DEFAULT NULL COMMENT '/* 销售部门, 外键 ( 参照 DEPT 表 ) */ ',
  PRIMARY KEY (`Sale_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT=' /* 销售 表 */ ';

-- ----------------------------
-- Records of Sale
-- ----------------------------
INSERT INTO `Sale` VALUES ('1', '2017-02-27 15:02:59', '1', '1');
INSERT INTO `Sale` VALUES ('2', '2017-03-13 15:03:06', '2', '1');
INSERT INTO `Sale` VALUES ('3', '2017-01-11 15:03:12', '3', '1');
INSERT INTO `Sale` VALUES ('4', '2017-03-23 15:03:18', '4', '2');
INSERT INTO `Sale` VALUES ('5', '2017-03-23 15:03:21', '5', '2');
INSERT INTO `Sale` VALUES ('6', '2017-01-11 15:03:27', '6', '3');

-- ----------------------------
-- Table structure for `Sale_Detail`
-- ----------------------------
DROP TABLE IF EXISTS `Sale_Detail`;
CREATE TABLE `Sale_Detail` (
  `Sale_ID` int(11) NOT NULL COMMENT '/* 销售编号,主键, 外键 ( 参照 SALE 表 ) */',
  `Product_ID` int(11) NOT NULL COMMENT '/* 商品编号,主键, 外键 ( 参照 PRODUCT 表 ) */',
  `Quantity` int(11) NOT NULL COMMENT '/* 数量 */',
  `Price` double DEFAULT NULL COMMENT '/* 价格 */',
  `Discount` double DEFAULT NULL COMMENT '/* 折扣 */ ',
  `SaleOrder_ID` int(11) DEFAULT NULL COMMENT '/* 销售合同, 外键 ( 参照 SALEORDER 表 ) */',
  PRIMARY KEY (`Sale_ID`,`Product_ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT=' /* 销售明细 ( 验货表 ) */ \r\n\r\n/* SALEORDER_ID 为 NULL 时, 为现金销售 */  ';

-- ----------------------------
-- Records of Sale_Detail
-- ----------------------------
INSERT INTO `Sale_Detail` VALUES ('1', '1', '2', '4700', null, null);
INSERT INTO `Sale_Detail` VALUES ('1', '2', '3', '5200', null, null);
INSERT INTO `Sale_Detail` VALUES ('1', '3', '20', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('2', '1', '1', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('2', '2', '2', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('2', '3', '23', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('1', '4', '211', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('2', '5', '21', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('2', '4', '2', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('3', '1', '2', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('4', '5', '100', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('5', '3', '99', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('5', '4', '99', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('5', '5', '99', null, null, null);
INSERT INTO `Sale_Detail` VALUES ('3', '4', '3', null, null, null);

-- ----------------------------
-- Table structure for `table001`
-- ----------------------------
DROP TABLE IF EXISTS `table001`;
CREATE TABLE `table001` (
  `c_0` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`c_0`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of table001
-- ----------------------------
INSERT INTO `table001` VALUES ('1', 'eric');
INSERT INTO `table001` VALUES ('2', 'mebal');
INSERT INTO `table001` VALUES ('3', 'today');

-- ----------------------------
-- View structure for `Product_Total_Quantity`
-- ----------------------------
DROP VIEW IF EXISTS `Product_Total_Quantity`;
CREATE ALGORITHM=UNDEFINED DEFINER=`remoteuser001`@`%` SQL SECURITY DEFINER VIEW `Product_Total_Quantity` AS select `Product`.`Name` AS `Name`,sum(`Sale_Detail`.`Quantity`) AS `Total_Quan`,(`Product`.`Price` * sum(`Sale_Detail`.`Quantity`)) AS `Total_Money` from (`Sale_Detail` join `Product` on((`Sale_Detail`.`Product_ID` = `Product`.`Product_ID`))) group by `Sale_Detail`.`Product_ID`,`Product`.`Price` ;
