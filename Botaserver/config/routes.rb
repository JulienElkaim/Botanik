Rails.application.routes.draw do
  get 'pages/tutorial'
  #get 'users/home'
  get 'home', to: 'pages#home', as: :home
  root to: 'pages#home'

  # Generic syntax:
  # verb 'path', to: 'controller#action', as: :route_name
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
