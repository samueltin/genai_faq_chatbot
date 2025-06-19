# Variables
variable "resource_group_name" {
  description = "The name of the resource group."
  type        = string
  default     = "insur-faq-bot-rg"
}

variable "location" {
  description = "The Azure region to deploy resources."
  type        = string
  default     = "East US" # Choose a region that supports Azure OpenAI and GPT-4
}

variable "ai_search_service_name" {
  description = "The name of the Azure AI Search service."
  type        = string
  default     = "insur-faq-search-service"
}

variable "openai_account_name" {
  description = "The name of the Azure OpenAI account."
  type        = string
  default     = "insur-faq-openai-account"
}

variable "text_embedding_ada_002_deployment_name" {
  description = "The name for the text-embedding-ada-002 model deployment."
  type        = string
  default     = "text-embedding-ada-002"
}

variable "gpt4_deployment_name" {
  description = "The name for the gpt-4 model deployment."
  type        = string
  default     = "gpt-4.1"
}

variable "gpt4_model_version" {
  description = "The version of the GPT-4 model. Check Azure OpenAI documentation for available versions (e.g., '1106-Preview', '0613', 'turbo-2024-04-09')."
  type        = string
  default     = "2025-04-14" # Replace with a version available in your chosen region
}