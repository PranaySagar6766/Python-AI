from abc import ABC, abstractmethod


# Abstract Base Class for all Employee types
class Employee(ABC):
    """
    Abstract base class representing a generic employee.
    All employee types must inherit from this class.
    """

    # Constructor: Initialize common employee attributes
    def __init__(self, empid, name):
        """
        Initialize employee with ID and name.
        Using protected attributes (single underscore) for internal use.
        """
        self._empid = empid  # Protected attribute for employee ID
        self._name = name  # Protected attribute for employee name

    # Abstract method: Must be implemented by all subclasses
    @abstractmethod
    def calculate_gross(self):
        """
        Abstract method to calculate gross salary.
        Each employee type must implement their own calculation logic.
        """
        pass

    # String representation of the employee
    def __str__(self):
        """Return string representation of employee."""
        return f'{self._empid}, {self._name}'

    # Property decorators for controlled access to protected attributes
    @property
    def empid(self):
        """Getter for employee ID."""
        return self._empid

    @property
    def name(self):
        """Getter for employee name."""
        return self._name


# Concrete class for salaried employees
class SalariedEmployee(Employee):
    """
    Represents employees with fixed monthly salary.
    Inherits from Employee base class.
    """

    # Constructor: Initialize salaried employee attributes
    def __init__(self, empid, name, basic):
        """
        Initialize salaried employee with basic salary.
        Calls parent constructor using super().
        """
        super().__init__(empid, name)  # Call parent constructor
        self._basic = basic  # Protected attribute for basic salary

    # Implementation of abstract method
    def calculate_gross(self):
        """
        Calculate gross salary including HRA and DA.
        HRA = 40% of basic, DA = 12% of basic
        """
        hra = self._basic * 0.4  # House Rent Allowance (40%)
        da = self._basic * 0.12  # Dearness Allowance (12%)
        return self._basic + hra + da

    # Method to calculate net salary after deductions
    def calculate_net(self):
        """
        Calculate net salary after PF deduction.
        PF = 12% of gross salary
        """
        gross = self.calculate_gross()  # Get gross salary
        pf = gross * 0.12  # Provident Fund deduction (12%)
        return gross - pf

    # Property for accessing basic salary
    @property
    def basic(self):
        """Getter for basic salary."""
        return self._basic


# Concrete class for contract employees
class ContractedEmployee(Employee):
    """
    Represents employees working on contract basis.
    Payment calculated based on days worked and daily rate.
    """

    # Constructor: Initialize contract employee attributes
    def __init__(self, empid, name, days, rate):
        """
        Initialize contract employee with work details.
        Removed unused monthly_income parameter.
        """
        super().__init__(empid, name)  # Call parent constructor
        self._days = days  # Number of days worked
        self._rate = rate  # Daily rate

    # Implementation of required abstract method
    def calculate_gross(self):
        """
        Calculate gross income based on days and rate.
        For contract employees, gross = days * daily_rate
        """
        return self._days * self._rate

    # Additional method for contract-specific calculations
    def calculate_income(self):
        """
        Calculate total income (same as gross for contractors).
        Kept for backward compatibility.
        """
        return self.calculate_gross()

    # Properties for accessing contract details
    @property
    def days(self):
        """Getter for days worked."""
        return self._days

    @property
    def rate(self):
        """Getter for daily rate."""
        return self._rate


# Specialized class for managers (extends SalariedEmployee)
class Manager(SalariedEmployee):
    """
    Represents managers who receive additional allowances.
    Inherits from SalariedEmployee class.
    """

    # Constructor: Initialize manager with additional allowance
    def __init__(self, empid, name, basic, allowance):
        """
        Initialize manager with basic salary and special allowance.
        """
        super().__init__(empid, name, basic)  # Call parent constructor
        self._allowance = allowance  # Protected attribute for manager allowance

    # Override calculate_gross to include allowance
    def calculate_gross(self):
        """
        Calculate gross salary including allowance.
        Managers get basic + HRA + DA + special allowance
        """
        base_gross = super().calculate_gross()  # Get base calculation
        return base_gross + self._allowance  # Add manager allowance

    # Property for accessing allowance
    @property
    def allowance(self):
        """Getter for manager allowance."""
        return self._allowance
