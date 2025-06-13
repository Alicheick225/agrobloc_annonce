-- Table annonces_vente
CREATE TABLE annonces_vente (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,           -- ID du producteur (provenant du service utilisateur)
    produit_id UUID NOT NULL,        -- ID du produit concerné
    prevision BOOLEAN DEFAULT FALSE,
    statut VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Table proposition_achat
CREATE TABLE proposition_achat (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,           -- ID de l'acheteur (provenant du service utilisateur)
    type_culture_id UUID NOT NULL,   -- Référence à un type de culture
    quantite INTEGER NOT NULL,
    statut VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Table commandes
CREATE TABLE commandes (
    id UUID PRIMARY KEY,
    annonce_vente_id UUID NOT NULL,  -- Référence à une annonce
    acheteur_id UUID NOT NULL,       -- ID de l’acheteur (depuis le service utilisateur)
    quantite INTEGER NOT NULL,
    statut VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Table candidatures
CREATE TABLE candidatures (
    id UUID PRIMARY KEY,
    proposition_achat_id UUID NOT NULL, -- Référence à une proposition d'achat
    producteur_id UUID NOT NULL,        -- ID du producteur (depuis le service utilisateur)
    statut VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
