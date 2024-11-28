-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 28-11-2024 a las 17:00:04
-- Versión del servidor: 5.7.44-log
-- Versión de PHP: 7.4.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fdpn`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `idp` int(11) NOT NULL,
  `nombrep` varchar(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `ocupacion` varchar(20) COLLATE utf8mb4_spanish_ci NOT NULL,
  `descripcion` varchar(200) COLLATE utf8mb4_spanish_ci NOT NULL,
  `precio` varchar(10) COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `correo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `clave` varchar(200) COLLATE utf8_spanish_ci NOT NULL,
  `fechareg` datetime NOT NULL,
  `perfil` char(1) COLLATE utf8_spanish_ci NOT NULL DEFAULT 'U'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `correo`, `clave`, `fechareg`, `perfil`) VALUES
(1, 'Liam 2', 'liam.mortera1789@alumnos.udg.mx', 'scrypt:32768:8:1$pBNv64kOahdwSF85$874f6ce0ded4462f4a45c1a3d7bc51672ea29a77fd11cd6f48bf89359b556e443a707a135b22ff866df135b0fa9cfbe007568594888fe913101ffe457540544e', '2024-11-27 12:29:19', 'U'),
(2, 'Liam ', 'liam.mortera1789@alumnos.udg.mx', 'scrypt:32768:8:1$56fqERxRveqhuABL$9b06b1059ee39b24a91e439b430a1e38e0bda1a5b39a3e6983837f37e499527596eb561307c16b171c645c9f78dcaedddb123e90259a0ef062125ea7785125c7', '2024-11-27 12:36:03', 'U'),
(3, 'Liam ', 'liam.mortera1789@alumnos.udg.mx', 'scrypt:32768:8:1$qx1z8yaNYsCVlnmX$e7cc0b9de6cbc757e59f2d7a2bc24b872602836f5ffa37be1811e5776e6e3b98754e48eaf15d5f0514a5c295d2937bf467369d87aa9c5697c16cc76ac311d83d', '2024-11-27 12:39:51', 'U'),
(4, 'Liam ', 'liam.mortera1789@alumnos.udg.mx', 'scrypt:32768:8:1$jcieU97UYx0fFrRN$33156875610afceccf2d4a427daf11afa039939cbbab7f001a5fde507bfdcaf176a6939fbbb9ea4ea24e9d5b313e9bbb09a625ce5a8640aa2ab6e6d4d40597b8', '2024-11-27 12:42:40', 'U'),
(5, 'Liam ', 'liam.mortera1789@alumnos.udg.mx', 'scrypt:32768:8:1$M2vIlcU6ewmSKOPF$bebf427dfc7414fb03f1cf66a857ef42052888b69701b5e374fb0e5ab888aaff9f6f094879bed3002e7bc039bd0488690c4e512d3393ba4caff84bd235d30b8b', '2024-11-27 12:43:49', 'U'),
(6, 'Liam ', 'liam.mortera1789@alumnos.udg.mx', 'scrypt:32768:8:1$XEUuz2rjSSAEgw1S$c75db8b9303059e8d78f69d0d863f6f3162de77473e6c0c77f0ce55352fa2e6d5d4aa99dde66a5f70d2206e7d63801bc9f629266f202382de1481707f5a44f67', '2024-11-28 10:20:46', 'U'),
(7, 'Liam ', 'liam.mortera1789@alumnos.udg.mx', 'scrypt:32768:8:1$DqsXQYyuEQ22grDc$6920d3a03f1877a80a871e0ff9b230bb8f6a9fd8f0cb891b33d41812dca0278078a2e153cdde52c7e629a41545fb4788f5bc73ad3adb41434eb6e053cbfcc0b2', '2024-11-28 10:32:21', 'U'),
(8, 'samuel', 'samuel.nav.car@gmail.com', 'scrypt:32768:8:1$0qfBW6FZjQCDxBGi$87605aa6290dc3c5cbbc3a7864e9e99b2b97fa650a0bc91f0c2b74e29af12c8f4b2c96e3f695c51e7a5fd70aa2587d1696bff84296525f84f3055e7fb634a034', '2024-11-28 10:33:31', 'U'),
(9, 'pedro', 'fernando.prieto2229@alumnos.udg.mx', 'scrypt:32768:8:1$kAgQdtkeQbkvfrIL$f73be5269d93dad9e9321f6380fe28c51fceb023d6510765a393a0ea89aeb5c91694be3c92ecb8d557754fde735cd48c475842f67c406200daf46adf76ccbd43', '2024-11-28 10:42:14', 'A');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`idp`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `producto`
--
ALTER TABLE `producto`
  MODIFY `idp` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
