-- This script was generated by the ERD tool in pgAdmin 4.
-- Creación de tablas
BEGIN;
CREATE TABLE IF NOT EXISTS public.apps_common_utils_requestlog
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    requests jsonb,
    CONSTRAINT apps_common_utils_requestlog_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_author
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    name character varying(250) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT apps_project_author_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_book
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    title character varying(255) COLLATE pg_catalog."default" NOT NULL,
    publication_date date NOT NULL,
    is_available boolean NOT NULL,
    CONSTRAINT apps_project_book_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_book_author
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    bookmodel_id bigint NOT NULL,
    authormodel_id bigint NOT NULL,
    CONSTRAINT apps_project_book_author_pkey PRIMARY KEY (id),
    CONSTRAINT apps_project_book_author_bookmodel_id_authormodel_2484e8b9_uniq UNIQUE (bookmodel_id, authormodel_id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_book_genre
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    bookmodel_id bigint NOT NULL,
    genremodel_id bigint NOT NULL,
    CONSTRAINT apps_project_book_genre_pkey PRIMARY KEY (id),
    CONSTRAINT apps_project_book_genre_bookmodel_id_genremodel__100fb82e_uniq UNIQUE (bookmodel_id, genremodel_id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_career
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT apps_project_career_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_common_user
(
    password character varying(128) COLLATE pg_catalog."default" NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) COLLATE pg_catalog."default" NOT NULL,
    first_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    last_name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    email character varying(254) COLLATE pg_catalog."default" NOT NULL,
    is_staff boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    id uuid NOT NULL,
    is_teacher boolean NOT NULL,
    is_student boolean NOT NULL,
    identification_card character varying(100) COLLATE pg_catalog."default" NOT NULL,
    cell_phone character varying(15) COLLATE pg_catalog."default",
    birthday date,
    address text COLLATE pg_catalog."default",
    career_id bigint,
    department_id bigint,
    CONSTRAINT apps_project_common_user_pkey PRIMARY KEY (id),
    CONSTRAINT apps_project_common_user_username_key UNIQUE (username)
);
CREATE TABLE IF NOT EXISTS public.apps_project_common_user_groups
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    usermodel_id uuid NOT NULL,
    group_id integer NOT NULL,
    CONSTRAINT apps_project_common_user_groups_pkey PRIMARY KEY (id),
    CONSTRAINT apps_project_common_user_usermodel_id_group_id_d9917839_uniq UNIQUE (usermodel_id, group_id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_common_user_user_permissions
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    usermodel_id uuid NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT apps_project_common_user_user_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT apps_project_common_user_usermodel_id_permission__0fd1abb8_uniq UNIQUE (usermodel_id, permission_id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_department
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT apps_project_department_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_fine
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    date date NOT NULL,
    amount numeric(10, 2) NOT NULL,
    book_id bigint NOT NULL,
    user_id uuid NOT NULL,
    CONSTRAINT apps_project_fine_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_genre
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT apps_project_genre_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_library_staff
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    is_chief_librarian boolean NOT NULL,
    department_id bigint,
    superior_id bigint,
    user_id uuid NOT NULL,
    CONSTRAINT apps_project_library_staff_pkey PRIMARY KEY (id),
    CONSTRAINT apps_project_library_staff_user_id_key UNIQUE (user_id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_loan
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    language character varying(50) COLLATE pg_catalog."default",
    created timestamp with time zone NOT NULL,
    updated timestamp with time zone NOT NULL,
    is_active boolean NOT NULL,
    default_order integer,
    start_date date NOT NULL,
    end_date date NOT NULL,
    status character varying(20) COLLATE pg_catalog."default" NOT NULL,
    user_id uuid NOT NULL,
    CONSTRAINT apps_project_loan_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.apps_project_loan_book
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    loanmodel_id bigint NOT NULL,
    bookmodel_id bigint NOT NULL,
    CONSTRAINT apps_project_loan_book_pkey PRIMARY KEY (id),
    CONSTRAINT apps_project_loan_book_loanmodel_id_bookmodel_id_a870d760_uniq UNIQUE (loanmodel_id, bookmodel_id)
);
CREATE TABLE IF NOT EXISTS public.auditlog_logentry
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    object_pk character varying(255) COLLATE pg_catalog."default" NOT NULL,
    object_id bigint,
    object_repr text COLLATE pg_catalog."default" NOT NULL,
    action smallint NOT NULL,
    changes text COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp with time zone NOT NULL,
    actor_id uuid,
    content_type_id integer NOT NULL,
    remote_addr inet,
    additional_data jsonb,
    serialized_data jsonb,
    CONSTRAINT auditlog_logentry_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.auth_group
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(150) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_group_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_name_key UNIQUE (name)
);
CREATE TABLE IF NOT EXISTS public.auth_group_permissions
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    group_id integer NOT NULL,
    permission_id integer NOT NULL,
    CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id),
    CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id)
);
CREATE TABLE IF NOT EXISTS public.auth_permission
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT auth_permission_pkey PRIMARY KEY (id),
    CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename)
);
CREATE TABLE IF NOT EXISTS public.authtoken_token
(
    key character varying(40) COLLATE pg_catalog."default" NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id uuid NOT NULL,
    CONSTRAINT authtoken_token_pkey PRIMARY KEY (key),
    CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id)
);
CREATE TABLE IF NOT EXISTS public.django_admin_log
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    action_time timestamp with time zone NOT NULL,
    object_id text COLLATE pg_catalog."default",
    object_repr character varying(200) COLLATE pg_catalog."default" NOT NULL,
    action_flag smallint NOT NULL,
    change_message text COLLATE pg_catalog."default" NOT NULL,
    content_type_id integer,
    user_id uuid NOT NULL,
    CONSTRAINT django_admin_log_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.django_content_type
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    app_label character varying(100) COLLATE pg_catalog."default" NOT NULL,
    model character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT django_content_type_pkey PRIMARY KEY (id),
    CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model)
);
CREATE TABLE IF NOT EXISTS public.django_migrations
(
    id bigint NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1 ),
    app character varying(255) COLLATE pg_catalog."default" NOT NULL,
    name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    applied timestamp with time zone NOT NULL,
    CONSTRAINT django_migrations_pkey PRIMARY KEY (id)
);
CREATE TABLE IF NOT EXISTS public.django_session
(
    session_key character varying(40) COLLATE pg_catalog."default" NOT NULL,
    session_data text COLLATE pg_catalog."default" NOT NULL,
    expire_date timestamp with time zone NOT NULL,
    CONSTRAINT django_session_pkey PRIMARY KEY (session_key)
);
CREATE TABLE IF NOT EXISTS public.django_site
(
    id integer NOT NULL GENERATED BY DEFAULT AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    domain character varying(100) COLLATE pg_catalog."default" NOT NULL,
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT django_site_pkey PRIMARY KEY (id),
    CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain)
);
ALTER TABLE IF EXISTS public.apps_project_book_author
    ADD CONSTRAINT apps_project_book_au_authormodel_id_3a8d94ff_fk_apps_proj FOREIGN KEY (authormodel_id)
    REFERENCES public.apps_project_author (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_book_author_authormodel_id_3a8d94ff
    ON public.apps_project_book_author(authormodel_id);
ALTER TABLE IF EXISTS public.apps_project_book_author
    ADD CONSTRAINT apps_project_book_au_bookmodel_id_b1143232_fk_apps_proj FOREIGN KEY (bookmodel_id)
    REFERENCES public.apps_project_book (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_book_author_bookmodel_id_b1143232
    ON public.apps_project_book_author(bookmodel_id);
ALTER TABLE IF EXISTS public.apps_project_book_genre
    ADD CONSTRAINT apps_project_book_ge_bookmodel_id_45a0b91a_fk_apps_proj FOREIGN KEY (bookmodel_id)
    REFERENCES public.apps_project_book (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_book_genre_bookmodel_id_45a0b91a
    ON public.apps_project_book_genre(bookmodel_id);
ALTER TABLE IF EXISTS public.apps_project_book_genre
    ADD CONSTRAINT apps_project_book_ge_genremodel_id_f12182b8_fk_apps_proj FOREIGN KEY (genremodel_id)
    REFERENCES public.apps_project_genre (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_book_genre_genremodel_id_f12182b8
    ON public.apps_project_book_genre(genremodel_id);
ALTER TABLE IF EXISTS public.apps_project_common_user
    ADD CONSTRAINT apps_project_common__career_id_c55dcec3_fk_apps_proj FOREIGN KEY (career_id)
    REFERENCES public.apps_project_career (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_common_user_career_id_c55dcec3
    ON public.apps_project_common_user(career_id);
ALTER TABLE IF EXISTS public.apps_project_common_user
    ADD CONSTRAINT apps_project_common__department_id_267d51f9_fk_apps_proj FOREIGN KEY (department_id)
    REFERENCES public.apps_project_department (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_common_user_department_id_267d51f9
    ON public.apps_project_common_user(department_id);
ALTER TABLE IF EXISTS public.apps_project_common_user_groups
    ADD CONSTRAINT apps_project_common__group_id_d3318472_fk_auth_grou FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_common_user_groups_group_id_d3318472
    ON public.apps_project_common_user_groups(group_id);
ALTER TABLE IF EXISTS public.apps_project_common_user_groups
    ADD CONSTRAINT apps_project_common__usermodel_id_bc9a3aa3_fk_apps_proj FOREIGN KEY (usermodel_id)
    REFERENCES public.apps_project_common_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_common_user_groups_usermodel_id_bc9a3aa3
    ON public.apps_project_common_user_groups(usermodel_id);
ALTER TABLE IF EXISTS public.apps_project_common_user_user_permissions
    ADD CONSTRAINT apps_project_common__permission_id_1c1475e8_fk_auth_perm FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_common_user_u_permission_id_1c1475e8
    ON public.apps_project_common_user_user_permissions(permission_id);
ALTER TABLE IF EXISTS public.apps_project_common_user_user_permissions
    ADD CONSTRAINT apps_project_common__usermodel_id_f8afa62d_fk_apps_proj FOREIGN KEY (usermodel_id)
    REFERENCES public.apps_project_common_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_common_user_user_permissions_usermodel_id_f8afa62d
    ON public.apps_project_common_user_user_permissions(usermodel_id);
ALTER TABLE IF EXISTS public.apps_project_fine
    ADD CONSTRAINT apps_project_fine_book_id_520dbbd1_fk_apps_project_book_id FOREIGN KEY (book_id)
    REFERENCES public.apps_project_book (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_fine_book_id_520dbbd1
    ON public.apps_project_fine(book_id);
ALTER TABLE IF EXISTS public.apps_project_fine
    ADD CONSTRAINT apps_project_fine_user_id_87526064_fk_apps_proj FOREIGN KEY (user_id)
    REFERENCES public.apps_project_common_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_fine_user_id_87526064
    ON public.apps_project_fine(user_id);
ALTER TABLE IF EXISTS public.apps_project_library_staff
    ADD CONSTRAINT apps_project_library_department_id_3f93b5b7_fk_apps_proj FOREIGN KEY (department_id)
    REFERENCES public.apps_project_department (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_library_staff_department_id_3f93b5b7
    ON public.apps_project_library_staff(department_id);
ALTER TABLE IF EXISTS public.apps_project_library_staff
    ADD CONSTRAINT apps_project_library_superior_id_1f711d50_fk_apps_proj FOREIGN KEY (superior_id)
    REFERENCES public.apps_project_library_staff (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_library_staff_superior_id_1f711d50
    ON public.apps_project_library_staff(superior_id);
ALTER TABLE IF EXISTS public.apps_project_library_staff
    ADD CONSTRAINT apps_project_library_user_id_b649b448_fk_apps_proj FOREIGN KEY (user_id)
    REFERENCES public.apps_project_common_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_library_staff_user_id_key
    ON public.apps_project_library_staff(user_id);
ALTER TABLE IF EXISTS public.apps_project_loan
    ADD CONSTRAINT apps_project_loan_user_id_800494a6_fk_apps_proj FOREIGN KEY (user_id)
    REFERENCES public.apps_project_common_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_loan_user_id_800494a6
    ON public.apps_project_loan(user_id);
ALTER TABLE IF EXISTS public.apps_project_loan_book
    ADD CONSTRAINT apps_project_loan_bo_bookmodel_id_84628974_fk_apps_proj FOREIGN KEY (bookmodel_id)
    REFERENCES public.apps_project_book (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_loan_book_bookmodel_id_84628974
    ON public.apps_project_loan_book(bookmodel_id);
ALTER TABLE IF EXISTS public.apps_project_loan_book
    ADD CONSTRAINT apps_project_loan_bo_loanmodel_id_bfcc5d15_fk_apps_proj FOREIGN KEY (loanmodel_id)
    REFERENCES public.apps_project_loan (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS apps_project_loan_book_loanmodel_id_bfcc5d15
    ON public.apps_project_loan_book(loanmodel_id);
ALTER TABLE IF EXISTS public.auditlog_logentry
    ADD CONSTRAINT auditlog_logentry_actor_id_959271d2_fk_apps_proj FOREIGN KEY (actor_id)
    REFERENCES public.apps_project_common_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auditlog_logentry_actor_id_959271d2
    ON public.auditlog_logentry(actor_id);
ALTER TABLE IF EXISTS public.auditlog_logentry
    ADD CONSTRAINT auditlog_logentry_content_type_id_75830218_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auditlog_logentry_content_type_id_75830218
    ON public.auditlog_logentry(content_type_id);
ALTER TABLE IF EXISTS public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id)
    REFERENCES public.auth_permission (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_group_permissions_permission_id_84c5c92e
    ON public.auth_group_permissions(permission_id);
ALTER TABLE IF EXISTS public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id)
    REFERENCES public.auth_group (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_group_permissions_group_id_b120cbf9
    ON public.auth_group_permissions(group_id);
ALTER TABLE IF EXISTS public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS auth_permission_content_type_id_2f476e4b
    ON public.auth_permission(content_type_id);
ALTER TABLE IF EXISTS public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_apps_project_common_user_id FOREIGN KEY (user_id)
    REFERENCES public.apps_project_common_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS authtoken_token_user_id_key
    ON public.authtoken_token(user_id);
ALTER TABLE IF EXISTS public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id)
    REFERENCES public.django_content_type (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS django_admin_log_content_type_id_c4bce8eb
    ON public.django_admin_log(content_type_id);
ALTER TABLE IF EXISTS public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_apps_proj FOREIGN KEY (user_id)
    REFERENCES public.apps_project_common_user (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX IF NOT EXISTS django_admin_log_user_id_c564eba6
    ON public.django_admin_log(user_id);
END;

-- Vistas
-- 1. Listado de Personal de Biblioteca con Libros Prestados y Cantidad Acumulada de Préstamos Realizados
CREATE VIEW library_staff_with_loans AS
SELECT 
    ls.id AS staff_id,
    cu.first_name,
    cu.last_name,
    cu.identification_card,
    cu.department_id,
    b.title AS book_title,
    COUNT(l.id) AS total_loans
FROM 
    apps_project_library_staff ls
JOIN 
    apps_project_common_user cu ON ls.user_id = cu.id
JOIN 
    apps_project_loan l ON l.user_id = cu.id
JOIN 
    apps_project_loan_book lb ON lb.loanmodel_id = l.id
JOIN 
    apps_project_book b ON lb.bookmodel_id = b.id
GROUP BY 
    ls.id, cu.first_name, cu.last_name, cu.identification_card, cu.department_id, b.title;

-- 2. Listado de Usuarios con Libros Prestados y Multas Acumuladas
CREATE VIEW users_with_loans_and_fines AS
SELECT 
    cu.id AS user_id,
    cu.first_name,
    cu.last_name,
    cu.identification_card,
    b.title AS book_title,
    SUM(f.amount) AS total_fines
FROM 
    apps_project_common_user cu
JOIN 
    apps_project_loan l ON l.user_id = cu.id
JOIN 
    apps_project_loan_book lb ON lb.loanmodel_id = l.id
JOIN 
    apps_project_book b ON lb.bookmodel_id = b.id
LEFT JOIN 
    apps_project_fine f ON f.user_id = cu.id AND f.book_id = b.id
GROUP BY 
    cu.id, cu.first_name, cu.last_name, cu.identification_card, b.title;

-- 3. Listado de Libros Disponibles y Cantidad de Préstamos Realizados
CREATE VIEW available_books_with_loan_count AS
SELECT 
    b.id AS book_id,
    b.title,
    b.is_available,
    COUNT(lb.loanmodel_id) AS total_loans
FROM 
    apps_project_book b
LEFT JOIN 
    apps_project_loan_book lb ON lb.bookmodel_id = b.id
GROUP BY 
    b.id, b.title, b.is_available
HAVING 
    b.is_available = TRUE;

-- 4. Listado de Personal de Biblioteca con Libros y Préstamos Acumulados
CREATE VIEW library_staff_with_books_and_total_loans AS
SELECT 
    ls.id AS staff_id,
    cu.first_name,
    cu.last_name,
    cu.identification_card,
    cu.department_id,
    COUNT(lb.bookmodel_id) AS total_books_loaned,
    COUNT(l.id) AS total_loans
FROM 
    apps_project_library_staff ls
JOIN 
    apps_project_common_user cu ON ls.user_id = cu.id
JOIN 
    apps_project_loan l ON l.user_id = cu.id
JOIN 
    apps_project_loan_book lb ON lb.loanmodel_id = l.id
GROUP BY 
    ls.id, cu.first_name, cu.last_name, cu.identification_card, cu.department_id;

-- 5. Listado de Multas Detallado
CREATE VIEW detailed_fines AS
SELECT 
    f.id AS fine_id,
    f.date,
    f.amount,
    cu.first_name AS user_first_name,
    cu.last_name AS user_last_name,
    cu.identification_card,
    b.title AS book_title
FROM 
    apps_project_fine f
JOIN 
    apps_project_common_user cu ON f.user_id = cu.id
JOIN 
    apps_project_book b ON f.book_id = b.id;


-- Consultas
-- 1. Información Completa de Personal de Biblioteca y Libros Prestados
SELECT 
    ls.id AS staff_id, cu.identification_card, cu.first_name, cu.last_name, cu.email, cu.cell_phone, cu.address, d.name AS department, 
    b.id AS book_id, b.title, b.publication_date, b.is_available, 
    l.start_date, l.end_date, l.status
FROM 
    apps_project_library_staff ls
JOIN 
    apps_project_common_user cu ON ls.user_id = cu.id
JOIN 
    apps_project_loan l ON l.user_id = cu.id
JOIN 
    apps_project_loan_book lb ON l.id = lb.loanmodel_id
JOIN 
    apps_project_book b ON lb.bookmodel_id = b.id
JOIN 
    apps_project_department d ON ls.department_id = d.id;

-- 2. Información Completa de Usuarios, Libros Prestados y Multas
SELECT 
    cu.id AS user_id, cu.identification_card, cu.first_name, cu.last_name, cu.email, cu.cell_phone, cu.address, 
    b.id AS book_id, b.title, b.publication_date, b.is_available, 
    l.start_date, l.end_date, l.status, 
    f.date AS fine_date, f.amount AS fine_amount
FROM 
    apps_project_common_user cu
JOIN 
    apps_project_loan l ON cu.id = l.user_id
JOIN 
    apps_project_loan_book lb ON l.id = lb.loanmodel_id
JOIN 
    apps_project_book b ON lb.bookmodel_id = b.id
LEFT JOIN 
    apps_project_fine f ON cu.id = f.user_id AND b.id = f.book_id;

-- 3. Libros Disponibles y Cantidad de Préstamos en un Día Específico
-- Reemplazar YYYY-MM-DD por la fecha a buscar
SELECT 
    b.id AS book_id, b.title, b.publication_date, b.is_available, 
    COUNT(l.id) AS total_loans
FROM 
    apps_project_book b
LEFT JOIN 
    apps_project_loan_book lb ON b.id = lb.bookmodel_id
LEFT JOIN 
    apps_project_loan l ON lb.loanmodel_id = l.id AND l.start_date = 'YYYY-MM-DD'
WHERE 
    b.is_available = TRUE
GROUP BY 
    b.id;

-- 4. Personal de Biblioteca con Libros y Préstamos Acumulados
SELECT 
    ls.id AS staff_id, cu.identification_card, cu.first_name, cu.last_name, cu.email, cu.cell_phone, cu.address, d.name AS department, 
    COUNT(l.id) AS total_loans, COUNT(DISTINCT lb.bookmodel_id) AS total_books
FROM 
    apps_project_library_staff ls
JOIN 
    apps_project_common_user cu ON ls.user_id = cu.id
LEFT JOIN 
    apps_project_loan l ON cu.id = l.user_id
LEFT JOIN 
    apps_project_loan_book lb ON l.id = lb.loanmodel_id
LEFT JOIN 
    apps_project_book b ON lb.bookmodel_id = b.id
JOIN 
    apps_project_department d ON ls.department_id = d.id
GROUP BY 
    ls.id, cu.identification_card, cu.first_name, cu.last_name, cu.email, cu.cell_phone, cu.address, d.name;

-- 5. Información Completa de Multas
SELECT 
    f.id AS fine_id, f.date AS fine_date, f.amount AS fine_amount, 
    cu.id AS user_id, cu.identification_card, cu.first_name, cu.last_name, cu.email, cu.cell_phone, cu.address, 
    b.id AS book_id, b.title, b.publication_date
FROM 
    apps_project_fine f
JOIN 
    apps_project_common_user cu ON f.user_id = cu.id
JOIN 
    apps_project_book b ON f.book_id = b.id;
