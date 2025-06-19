# Outputs
output "resource_group_name" {
  description = "The name of the deployed Resource Group."
  value       = azurerm_resource_group.main.name
}

output "ai_search_service_name" {
  description = "The name of the deployed Azure AI Search service."
  value       = azurerm_search_service.main.name
}

output "openai_account_name" {
  description = "The name of the deployed Azure OpenAI account."
  value       = azurerm_cognitive_account.openai.name
}

output "openai_account_endpoint" {
  description = "The endpoint URL for the Azure OpenAI account."
  value       = azurerm_cognitive_account.openai.endpoint
}

output "text_embedding_ada_002_deployment_name" {
  description = "The name of the text-embedding-ada-002 deployment."
  value       = azurerm_cognitive_deployment.text_embedding_ada_002.name
}

output "gpt4_deployment_name" {
  description = "The name of the gpt-4 deployment."
  value       = azurerm_cognitive_deployment.gpt4.name
}