CREATE TABLE `students` (`studentId` int(11) NOT NULL AUTO_INCREMENT,
                                                      `firstName` varchar(50) NOT NULL,
                                                                              `lastName` varchar(50) NOT NULL,
                                                                                                     `dob` date NOT NULL,
                                                                                                                `amountDue` int(11) NOT NULL,
                                                                                                                                    PRIMARY KEY (`studentId`)) ENGINE=InnoDB DEFAULT
CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

