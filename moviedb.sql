--
-- PostgreSQL database dump
--

-- Dumped from database version 10.18
-- Dumped by pg_dump version 10.18

-- Started on 2021-09-08 14:01:22

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12924)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2817 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 199 (class 1259 OID 16815)
-- Name: director; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.director (
    director_id integer NOT NULL,
    name character varying(50) NOT NULL,
    imdb_link character varying(100) NOT NULL
);


ALTER TABLE public.director OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16813)
-- Name: director_director_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.director_director_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.director_director_id_seq OWNER TO postgres;

--
-- TOC entry 2818 (class 0 OID 0)
-- Dependencies: 198
-- Name: director_director_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.director_director_id_seq OWNED BY public.director.director_id;


--
-- TOC entry 197 (class 1259 OID 16802)
-- Name: movie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movie (
    movie_id integer NOT NULL,
    title character varying(100) NOT NULL,
    description character varying(1000) NOT NULL,
    original_title character varying(100) NOT NULL
);


ALTER TABLE public.movie OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16827)
-- Name: movie_director; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movie_director (
    movie_id integer NOT NULL,
    director_id integer NOT NULL
);


ALTER TABLE public.movie_director OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16800)
-- Name: movie_movie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.movie_movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movie_movie_id_seq OWNER TO postgres;

--
-- TOC entry 2819 (class 0 OID 0)
-- Dependencies: 196
-- Name: movie_movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.movie_movie_id_seq OWNED BY public.movie.movie_id;


--
-- TOC entry 2682 (class 2604 OID 16849)
-- Name: director director_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director ALTER COLUMN director_id SET DEFAULT nextval('public.director_director_id_seq'::regclass);


--
-- TOC entry 2681 (class 2604 OID 16841)
-- Name: movie movie_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie ALTER COLUMN movie_id SET DEFAULT nextval('public.movie_movie_id_seq'::regclass);


--
-- TOC entry 2686 (class 2606 OID 16851)
-- Name: director director_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.director
    ADD CONSTRAINT director_pkey PRIMARY KEY (director_id);


--
-- TOC entry 2684 (class 2606 OID 16843)
-- Name: movie movie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (movie_id);


--
-- TOC entry 2688 (class 2606 OID 16852)
-- Name: movie_director fk_director_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_director
    ADD CONSTRAINT fk_director_id FOREIGN KEY (director_id) REFERENCES public.director(director_id);


--
-- TOC entry 2687 (class 2606 OID 16844)
-- Name: movie_director fk_movie_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie_director
    ADD CONSTRAINT fk_movie_id FOREIGN KEY (movie_id) REFERENCES public.movie(movie_id);


-- Completed on 2021-09-08 14:01:24

--
-- PostgreSQL database dump complete
--

