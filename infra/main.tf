# Resource Group
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
}

# Azure AI Search Service
resource "azurerm_search_service" "main" {
  name                = var.ai_search_service_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  sku                 = "free" # Choose a suitable SKU (e.g., free, basic, standard)
  replica_count       = 1
  partition_count     = 1
}

# Azure OpenAI Account (Cognitive Account with kind = "OpenAI")
resource "azurerm_cognitive_account" "openai" {
  name                = var.openai_account_name
  resource_group_name = azurerm_resource_group.main.name
  location            = azurerm_resource_group.main.location
  kind                = "OpenAI"
  sku_name            = "S0" # S0 is the standard SKU for OpenAI
}

# Azure OpenAI Deployment for text-embedding-ada-002
resource "azurerm_cognitive_deployment" "text_embedding_ada_002" {
  name                 = var.text_embedding_ada_002_deployment_name
  cognitive_account_id = azurerm_cognitive_account.openai.id

  model {
    format = "OpenAI"
    name   = "text-embedding-ada-002"
    version = "2" # Specific version for text-embedding-ada-002
  }

  sku {
    name     = "GlobalStandard"
  }
}

# Azure OpenAI Deployment for gpt-4
resource "azurerm_cognitive_deployment" "gpt4" {
  name                 = var.gpt4_deployment_name
  cognitive_account_id = azurerm_cognitive_account.openai.id

  model {
    format  = "OpenAI"
    name    = var.gpt4_deployment_name # Use the variable for deployment name
    version = var.gpt4_model_version # Use the variable for model version
  }

  sku {
    name     = "GlobalStandard"
  }
}