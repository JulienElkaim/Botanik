include ::TimeConcern
class Order < ApplicationRecord
  belongs_to :user
  belongs_to :network
  has_many :logs

  def self.convertTime(arg)
  	 puts Time::secondConverter(arg)
  end
end
