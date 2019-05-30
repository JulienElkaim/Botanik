class Network < ApplicationRecord
	has_many :accounts
	has_many :orders
end
