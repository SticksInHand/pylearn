CREATE TABLE `qkxt_user` (
  `ID` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '用户表自增ID',
  `UserName` varchar(255) NOT NULL COMMENT '用户名',
  `UserMobile` char(11) NOT NULL COMMENT '用户手机号',
  `UserEmail` varchar(100) NOT NULL COMMENT '用户邮箱',
  `UserImg` varchar(255) NOT NULL COMMENT '用户头像',
  `UserID` char(32) NOT NULL COMMENT '用户ID',
  `password` varchar(255) NOT NULL COMMENT '用户密码',
  `passhash` char(32) NOT NULL COMMENT '用户密码MD5',
  `token` char(32) NOT NULL COMMENT 'token',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8