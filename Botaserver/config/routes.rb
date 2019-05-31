Rails.application.routes.draw do
  #get 'users/home'
  get 'home', to: 'users#home', as: :home
  root to: 'users#home'

  # Generic syntax:
  # verb 'path', to: 'controller#action', as: :route_name
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
