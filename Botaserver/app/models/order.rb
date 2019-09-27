include ::TimeConcern
class Order < ApplicationRecord
  belongs_to :user
  belongs_to :network
  has_many :logs,  dependent: :delete_all

  def self.convertTime(arg)
  	return Time::secondConverter(arg)
  end

  def self.convertSeconds(arg)
  	return Time::integerConverter(arg)
  end
end
