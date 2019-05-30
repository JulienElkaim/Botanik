class Account < ApplicationRecord
  belongs_to :user
  belongs_to :network

  validates :user_id, uniqueness: { scope: :network_id}
end
