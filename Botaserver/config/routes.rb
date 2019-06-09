Rails.application.routes.draw do
  devise_for :users
  
  #get 'users/home'
  get 'dashboard', to: 'pages#dashboard', as: :home
  get 'autre', to: 'pages#autre', as: :autre
  # get 'networks', to: 'networks#index', as: :autre
  
  root to: 'pages#dashboard'

  resources :accounts

  #Orders objects
  get '/orders', to: 'orders#index', as: :orders

  # Generic syntax:
  # verb 'path', to: 'controller#action', as: :route_name
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
