-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-06-2024 a las 08:28:48
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

-- Base de datos: `datos_2`

-- Estructura de tabla para la tabla `bancos`

CREATE TABLE `bancos` (
  `codigo_banco` varchar(11) NOT NULL,
  `nombre_entidad` varchar(50) NOT NULL,
  `codigo_iban` varchar(34) NOT NULL,
  `codigo_swift` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estructura de tabla para la tabla `cliente`

CREATE TABLE `cliente` (
  `codigo_cliente` varchar(11) NOT NULL,
  `nombre` varchar(35) NOT NULL,
  `apellido` varchar(35) NOT NULL,
  `nif_nie` varchar(20) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `cp` varchar(5) NOT NULL,
  `poblacion` varchar(35) NOT NULL,
  `provincia` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- -- Volcado de datos para la tabla `cliente`

-- INSERT INTO `cliente` (`codigo_cliente`, `nombre`, `apellido`, `nif_nie`, `direccion`, `cp`, `provincia`) VALUES
-- (1, 'Juan', 'Perez', '12345678R', 'Calle Mayor 1', '08456', 'Barcelona'),
-- (2, 'Maria', 'Garcia', '87654321T', 'Calle Mayor 2', '08456', 'Barcelona'),
-- (3, 'Pedro', 'Gomez', '12345678R', 'Calle Mayor 3', '08456', 'Barcelona');

-- Estructura de tabla para la tabla `codigopostal`

CREATE TABLE `codigopostal` (
  `codigo` varchar(5) NOT NULL,
  `descripcion` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estructura de tabla para la tabla `direccionenvio`

CREATE TABLE `direccionenvio` (
  `cp` varchar(5) NOT NULL,
  `poblacion` varchar(35) NOT NULL,
  `provincia` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estructura de tabla para la tabla `vendedor`

CREATE TABLE `vendedor` (
  `nombre` varchar(35) NOT NULL,
  `cif` varchar(10) NOT NULL,
  `direccion` varchar(35) NOT NULL,
  `cp` varchar(5) NOT NULL,
  `poblacion` varchar(35) NOT NULL,
  `provincia` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- -- Volcado de datos para la tabla `vendedor`

-- INSERT INTO `vendedor` (`nombre_vendedor`, `cif`, `direccion_vendedor`, `cp`, `poblacion` `provincia`) VALUES
-- ('Los del Fondo', '12345678R', 'Carrer del Riu Anoia' '08456', 'El Prado del Llobregat', 'Barcelona');

-- Estructura de tabla para la tabla `lineas_factura

CREATE TABLE `lineas_factura` (
  `descripcion` varchar(100) NOT NULL,
  `cantidad` varchar(11) NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estructura de tabla para la tabla `poblacion`

CREATE TABLE `poblacion` (
  `codigo` varchar(3) NOT NULL,
  `descripcion` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estructura de tabla para la tabla `productos`

CREATE TABLE `productos` (
  `codigo_producto` varchar(11) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `cantidad` varchar(11) NOT NULL,
  `precio_unitario` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estructura de tabla para la tabla `provincias`

CREATE TABLE `provincias` (
  `codigo` varchar(2) NOT NULL,
  `descripción` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Estructura de tabla para la tabla `cabecera`
CREATE TABLE `cabecera` (
    -- vendedor
    `vendedor_nombre` varchar(35) NOT NULL,
    `vendedor_direccion` varchar(50) NOT NULL,
    `vendedor_cp` varchar(5) NOT NULL,
    `vendedor_poblacion` varchar(35) NOT NULL,
    `vendedor_provincia` varchar(35) NOT NULL,
    -- cliente
    `cliente_nombre` varchar(35) NOT NULL,
    `cliente_apellido` varchar(35) NOT NULL,
    `cliente_direccion` varchar(50) NOT NULL,
    `cliente_cp` varchar(5) NOT NULL,
    `cliente_poblacion` varchar(35) NOT NULL,
    `cliente_provincia` varchar(35) NOT NULL,
    -- direccionenvio
    `envio_nombre` varchar(35) NOT NULL,
    `envio_apellido` varchar(35) NOT NULL,
    `envio_direccion` varchar(50) NOT NULL,
    `envio_cp` varchar(5) NOT NULL,
    `envio_poblacion` varchar(35) NOT NULL,
    `envio_provincia` varchar(35) NOT NULL,
    -- bancos
    `nombre_entidad` varchar(50) NOT NULL,
    `codigo_iban` varchar(34) NOT NULL,
    `codigo_swift` varchar(11) NOT NULL,
    -- datos
    `numero_factura` varchar(11) NOT NULL,
    `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


-- Índices para tablas volcadas

-- Indices de la tabla `bancos`
ALTER TABLE `bancos`
  ADD PRIMARY KEY (`codigo_banco`);

-- Indices de la tabla `cliente`
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`codigo_cliente`);

-- Indices de la tabla `codigopostal`
ALTER TABLE `codigopostal`
  ADD PRIMARY KEY (`codigo`);

-- Indices de la tabla `direccionenvio`
ALTER TABLE `direccionenvio`
  ADD PRIMARY KEY (`id_envio`);

-- Indices de la tabla `vendedor`
ALTER TABLE `vendedor`
  ADD PRIMARY KEY (`cif`);

-- Indices de la tabla `lineas_factura`
ALTER TABLE `lineas_factura`
  ADD PRIMARY KEY (`numero_factura`);

-- Indices de la tabla `poblacion`
ALTER TABLE `poblacion`
  ADD PRIMARY KEY (`codigo`);

-- Indices de la tabla `productos`
ALTER TABLE `productos`
  ADD PRIMARY KEY (`codigo_producto`),
  ADD UNIQUE (`precio_unitario`);


-- Indices de la tabla `provincias`

ALTER TABLE `provincias`
  ADD PRIMARY KEY (`codigo`);

-- Filtros para la tabla `cliente`
ALTER TABLE `cliente`
  ADD CONSTRAINT `fk_cp_codigopostal` FOREIGN KEY (`cp`) REFERENCES `codigopostal` (`codigo`),
  ADD CONSTRAINT `fk_poblacion_poblacion` FOREIGN KEY (`poblacion`) REFERENCES `poblacion` (`codigo`),
  ADD CONSTRAINT `fk_provincia_provincias` FOREIGN KEY (`provincia`) REFERENCES `provincias` (`codigo`);

-- Filtros para la tabla `vendedor`
--
ALTER TABLE `vendedor`
  ADD CONSTRAINT `fk_cp_codigopostal` FOREIGN KEY (`cp`) REFERENCES `codigopostal` (`codigo`),
  ADD CONSTRAINT `fk_poblacion_poblacion` FOREIGN KEY (`poblacion`) REFERENCES `poblacion` (`codigo`),
  ADD CONSTRAINT `fk_provincia_provincias` FOREIGN KEY (`provincia`) REFERENCES `provincias` (`codigo`);

-- Filtros para la tabla `direccionenvio`
ALTER TABLE `direccionenvio`
  ADD CONSTRAINT `fk_cp_codigopostal` FOREIGN KEY (`cp`) REFERENCES `codigopostal` (`codigo`),
  ADD CONSTRAINT `fk_poblacion_poblacion` FOREIGN KEY (`poblacion`) REFERENCES `poblacion` (`codigo`),
  ADD CONSTRAINT `fk_provincia_provincias` FOREIGN KEY (`provincia`) REFERENCES `provincias` (`codigo`);

-- Filtros para la tabla `lineas_factura`
ALTER TABLE `lineas_factura`
  ADD CONSTRAINT `fk_productos_codigo_producto` FOREIGN KEY (`codigo_producto`) REFERENCES `productos` (`codigo_producto`),
  ADD CONSTRAINT `fk_productos_precio_unitario` FOREIGN KEY (`precio_unitario`) REFERENCES `productos` (`precio_unitario`);

-- Filtros para la tabla `poblacion`
ALTER TABLE `poblacion`
  ADD CONSTRAINT `fk_provincias` FOREIGN KEY (`codigo`) REFERENCES `provincias` (`codigo`),
  ADD CONSTRAINT `fk_poblacion` FOREIGN KEY (`codigo`) REFERENCES `codigopostal` (`codigo`);

-- Filtros para la tabla `provincias`
ALTER TABLE `provincias`
  ADD CONSTRAINT `fk_codigopostal` FOREIGN KEY (`codigo`) REFERENCES `codigopostal` (`codigo`),
COMMIT;

-- ADD CONSTRAINT `fk_cliente_codigo_cliente` FOREIGN KEY (`codigo_cliente`) REFERENCES `cliente` (`codigo_cliente`),

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
